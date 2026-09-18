/* eslint-disable max-classes-per-file */

/* Mocks of all parts of the electron API that we use.

None of the electron APIs are available in a node env, even though
electron is a node module. (Note that node_modules/electron/index.js only
exports the filepath to the electron exe.)

APIs are only available in an electron browser environment, but our tests
run in node where all electron's exports are undefined. So we must mock,
even for APIs that would otherwise seem okay to call during a test.
*/

import os from 'os';
import events from 'events';

import { vi } from 'vitest';

class MockIPC extends events.EventEmitter {
  constructor() {
    super();
    this.handle = vi.fn();
    this.invoke = vi.fn().mockImplementation(() => Promise.resolve());
    this.send = (channel, ...args) => {
      const event = {
        reply: (channel, response) => {
          this.emit(channel, {}, response);
        }
      };
      this.emit(channel, event, ...args);
    };
    this.sendSync = vi.fn();
  }
}
const electronMockIPC = new MockIPC();
export const ipcMain = electronMockIPC;
export const ipcRenderer = electronMockIPC;

class MockApp extends events.EventEmitter {
  constructor() {
    super();
    this.getPath = vi.fn().mockImplementation(
      () => os.tmpdir()
    );
    this.setPath = vi.fn();
    this.getName = vi.fn();
    this.getVersion = vi.fn();
  }
}
export const app = new MockApp();

export class BrowserWindow {
  constructor() {
    this.loadURL = vi.fn();
    this.once = vi.fn();
    this.on = vi.fn();
    this.webContents = {
      on: vi.fn(),
      session: {
        on: vi.fn(),
      },
      send: (channel, ...args) => {
        electronMockIPC.emit(channel, {}, ...args);
      },
      downloadURL: vi.fn(),
    };
  }
}

export const dialog = {
  showOpenDialog: vi.fn(),
  showSaveDialog: vi.fn(),
};

export const Menu = {
  buildFromTemplate: vi.fn(),
  setApplicationMenu: vi.fn(),
};

export const nativeTheme = {};

export const screen = {
  getPrimaryDisplay: vi.fn().mockReturnValue({
    workAreaSize: { width: 800, height: 800 }
  })
};

export const shell = {
  showItemInFolder: vi.fn(),
  openExternal: vi.fn(),
};

export const webUtils = {
  getPathForFile: vi.fn((file) => file.name),
};
