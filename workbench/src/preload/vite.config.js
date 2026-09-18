import { defineConfig } from 'vite';
import path from 'path';

const PROJECT_ROOT = '../..';

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    mode: process.env.MODE,
    sourcemap: 'inline',
    minify: false,
    outDir: path.join(PROJECT_ROOT, 'build/preload'),
    // target: 'chrome114',
    lib: {
      entry: 'preload.js',
      formats: ['cjs'],
      fileName: () => 'preload.js',
    },
    rollupOptions: {
      external: ['electron'], // Don't bundle electron
      // input: ['preload.js'],
      // output: {
      //   entryFileNames: 'preload.js',
      // },
    },
    emptyOutDir: true,
  },
});
