import React, { useEffect, useRef, useState } from 'react';
import ReactDom from 'react-dom';
import PropTypes from 'prop-types';

import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

import { ipcMainChannels } from '../../../main/ipcMainChannels';

const { ipcRenderer } = window.Workbench.electron;

export default function ResultsTab(props) {

  const [htmlContent, setHtmlContent] = useState('');

  useEffect(() => {
    async function loadHTML() {
      console.log(props.status)
      console.log(props.htmlFile)
      if (props.status === 'success') {
        const html = await ipcRenderer.invoke(
          ipcMainChannels.INVEST_READ_HTML,
          props.htmlFile,
        );
        // console.log(html)
        setHtmlContent(html);
      }
    }
    loadHTML();
  }, [props.status]);

  return (
    <Container fluid>
      {/*<iframe srcdoc={htmlContent} width="auto" height="auto" />*/}
      <Row>
        <iframe
          // srcdoc={htmlContent}
          src={props.htmlFile}
          style={{
            flex: "1 1 auto",
            height: "var(--content-height)",
            border: "none",
          }}
        />
      </Row>
      {/*<Row dangerouslySetInnerHTML={{__html: htmlContent}}>*/}
      {/*</Row>*/}
    </Container>
  );
}

ResultsTab.propTypes = {
  htmlFile: PropTypes.string,
  tabID: PropTypes.string.isRequired,
};
