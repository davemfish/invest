import { ipcMain } from 'electron';

import { ipcMainChannels } from './ipcMainChannels';

export default function removeIpcMainListeners() {
  Object.values(ipcMainChannels).forEach((channel) => {
    ipcMain.removeAllListeners(channel);
  });
}
