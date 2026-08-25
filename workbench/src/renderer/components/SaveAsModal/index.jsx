import React, { useState } from 'react';

import Stack from 'react-bootstrap/Stack';
import Alert from 'react-bootstrap/Alert';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import { MdSave, MdClose } from 'react-icons/md';
import { useTranslation } from 'react-i18next';

import {
  archiveDatastack,
  saveToPython,
  writeParametersToFile,
  writeMetadataFiles,
} from '../../server_requests';
import { ipcMainChannels } from '../../../main/ipcMainChannels';

const { ipcRenderer } = window.Workbench.electron;

/** Render a dialog with a form for configuring global invest settings */
export default function SaveAsModal(props) {
  const { modelID, args } = props;

  const [show, setShow] = useState(false);
  const [selection, setSelection] = useState('json');
  const [relativePaths, setRelativePaths] = useState(false);
  const [alertMessage, setAlertMessage] = useState('');
  const [alertError, setAlertError] = useState(false);
  const [disabledSave, setDisabledSave] = useState(false);

  function handleClose() {
    setShow(false);
    setAlertMessage('');
    setAlertError(false);
  }

  function handleShow() {
    setShow(true);
    setRelativePaths(false);
  }

  function handleChange(event) {
    setSelection(event.currentTarget.value);
  }

  function handleRelativePathsCheckbox(event) {
    setRelativePaths(event.target.checked);
  }

    /** Save the current invest arguments to a python script via datastack.py API.
   *
   * @param {string} filepath - desired path to the python script
   * @returns {undefined}
   */
  async function savePythonScript(filepath) {
    const payload = {
      filepath: filepath,
      model_id: modelID,
      args: JSON.stringify(args),
    };
    const { message, error } = await saveToPython(payload);
    setAlertMessage(message);
    setAlertError(error);
  }

  async function saveJsonFile(datastackPath) {
    const payload = {
      filepath: datastackPath,
      model_id: modelID,
      relativePaths: relativePaths,
      args: JSON.stringify(args),
    };
    const { message, error } = await writeParametersToFile(payload);
    setAlertMessage(message);
    setAlertError(error);
  }

  async function saveDatastack(datastackPath) {
    const payload = {
      filepath: datastackPath,
      model_id: modelID,
      args: JSON.stringify(args),
    };
    setAlertMessage('archiving...');
    const { message, error } = await archiveDatastack(payload);
    setAlertMessage(message);
    setAlertError(error);
  }

  async function exportMetadata() {
    const payload = {
      model_id: modelID,
      args: JSON.stringify(args),
    };
    const { message, error } = await writeMetadataFiles(payload);
    setAlertMessage(message);
    setAlertError(error);
  }

  async function browseSaveFile() {
    setDisabledSave(true);
    const defaultTargetPaths = {
      json: `invest_${modelID}_args.json`,
      tgz: `invest_${modelID}_datastack.tgz`,
      py: `execute_invest_${modelID}.py`,
    };

    if (selection === 'metadata') {
      exportMetadata();
    } else {
      const data = await ipcRenderer.invoke(
        ipcMainChannels.SHOW_SAVE_DIALOG,
        { defaultPath: defaultTargetPaths[selection] }
      );
      if (data.filePath) {
        switch (selection) {
          case 'json':
            saveJsonFile(data.filePath, relativePaths);
            break;
          case 'tgz':
            saveDatastack(data.filePath);
            break;
          case 'py':
            savePythonScript(data.filePath);
        }
      }
    }
    setDisabledSave(false);
  }

  const { t } = useTranslation();

  return (
    <React.Fragment>
      <Button
        aria-label="save-as"
        variant="link"
        onClick={handleShow}
      >
        <MdSave className="me-1 mb-1" />
        {t("Save as...")}
      </Button>

      <Modal
        className="save-as-modal"
        size="lg"
        show={show}
        onHide={handleClose}
      >
        <Modal.Header>
          <Modal.Title>{t('Datastack options')}</Modal.Title>
          <Button
            variant="secondary-outline"
            onClick={handleClose}
            aria-label="close save-as dialog"
          >
            <MdClose />
          </Button>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Check className="save-as-option">
              <Form.Check.Label>
                <Form.Check.Input
                  type="radio"
                  value="json"
                  checked={selection === 'json'}
                  name="datastackType"
                  id="datastackType-json"
                  className="text-start"
                  variant="light"
                  onChange={handleChange}
                />
                <span className="option-header">Parameters only</span>
                <Form.Text>
                  {t('Save your parameters in a JSON file. This includes the ' +
                    'paths to your input data, but not the data itself. ' +
                    'Open this file in InVEST to restore your parameters.')}
                </Form.Text>
                <Form.Check
                  id="relativePaths"
                  label="Use relative paths"
                  name="relativePaths"
                  disabled={selection !== 'json'}
                  onChange={handleRelativePathsCheckbox}
                />
              </Form.Check.Label>
            </Form.Check>
            <Form.Check className="save-as-option">
              <Form.Check.Label>
                <Form.Check.Input
                  type="radio"
                  value="tgz"
                  checked={selection === 'tgz'}
                  name="datastackType"
                  id="datastackType-tgz"
                  className="text-start"
                  variant="light"
                  onChange={handleChange}
                />
                <span className="option-header">Parameters and data</span>
                <Form.Text>
                  {t('Save your parameters and input data in a compressed archive. ' +
                    'This archive contains the same JSON file produced by the ' +
                    '"Parameters only" option, plus the data. You can open this ' +
                    'file in InVEST to restore your parameters. This option is ' +
                    'useful to copy all the necessary data to a different location.')}
                </Form.Text>
              </Form.Check.Label>
            </Form.Check>
            <Form.Check className="save-as-option">
              <Form.Check.Label>
                <Form.Check.Input
                  type="radio"
                  value="py"
                  checked={selection === 'py'}
                  name="datastackType"
                  id="datastackType-py"
                  className="text-start"
                  variant="light"
                  onChange={handleChange}
                />
                <span className="option-header">Python script</span>
                <Form.Text>
                  {t('Save your parameters in a python script. This includes the ' +
                    'paths to your input data, but not the data itself. Running ' +
                    'the python script will programmatically run the model with ' +
                    'your parameters. Use this as a starting point for batch scripts.')}
                </Form.Text>
              </Form.Check.Label>
            </Form.Check>
            <Form.Check className="save-as-option">
              <Form.Check.Label>
                <Form.Check.Input
                  type="radio"
                  value="metadata"
                  checked={selection === 'metadata'}
                  name="datastackType"
                  id="datastackType-metadata"
                  className="text-start"
                  variant="light"
                  onChange={handleChange}
                />
                <span className="option-header">Metadata</span>
                <Form.Text>
                  {t(`Save a metadata file for each dataset in the input parameters.
                      Metadata files are .yml files generated by GeoMetaMaker
                      and include descriptions and keywords associated with
                      the model’s input data specifications. Metadata for
                      model outputs are automatically generated when running
                      the model.`)}
                </Form.Text>
              </Form.Check.Label>
            </Form.Check>
            <Stack gap={2} direction="horizontal">
              <Button
                className="w-75"
                onClick={browseSaveFile}
                disabled={disabledSave}
              >
                <MdSave className="me-1" />
                {t('Save')}
              </Button>
              <Button
                className="w-25"
                variant="secondary"
                onClick={handleClose}
              >
                {t('Close')}
              </Button>
            </Stack>
            { (alertMessage) && (
              <Alert
                variant={alertError ? 'danger' : 'success'}
              >
                {t(alertMessage)}
              </Alert>
            )}
          </Form>
        </Modal.Body>
      </Modal>
    </React.Fragment>
  );
}
