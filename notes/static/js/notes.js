document.addEventListener('DOMContentLoaded', function() {
    const previewButtons = document.querySelectorAll('.preview-button');
    const previewWindow = document.getElementById('preview-window');
    const previewTitle = document.getElementById('preview-title');
    const previewNote = document.getElementById('preview-note');
    const closeButton = document.getElementById('close-button');

    previewButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const title = this.getAttribute('data-title');
            const content = this.getAttribute('data-content');
            previewTitle.innerText = title;
            previewNote.innerText = content;
            previewWindow.style.display = 'block';
        });
    });

    closeButton.addEventListener('click', function() {
        previewWindow.style.display = 'none';
    });
});
