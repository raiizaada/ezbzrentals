import { create, registerPlugin } from 'filepond';
import 'filepond/dist/filepond.css';

// Import the File Type Validation plugin
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';

// Register the plugin with FilePond
registerPlugin(FilePondPluginFileValidateType);

// Get a file input reference
const input = document.querySelector('input[type="file"]');

// Create a FilePond instance
create(input, {
    // Only accept images
    acceptedFileTypes: ['image/*'],

    fileValidateTypeDetectType: (source, type) =>
        new Promise((resolve, reject) => {
            // test if is xls file
            if (/\.xls$/.test(source.name)) return resolve('application/vnd.ms-excel');

            // accept detected type
            resolve(type);
        }),
});