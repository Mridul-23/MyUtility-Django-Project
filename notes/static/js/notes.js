document.addEventListener('DOMContentLoaded', function() {
    const noteRows = document.querySelectorAll('.note-row');
    const previewWindow = document.getElementById('preview-window');
    const previewTitle = document.getElementById('preview-title');
    const previewContent = document.getElementById('preview-content');
    const closeButton = document.getElementById('close-button');

    noteRows.forEach(row => {
        // Exclude click event for delete button
        const deleteButton = row.querySelector('.delete-button');
        if (deleteButton) {
            deleteButton.addEventListener('click', function(event) {
                event.stopPropagation(); 
            });
        }

        row.addEventListener('click', function() {
            if (!event.target.classList.contains('delete-button')) {
                const title = this.children[1].innerText; 
                const content = this.getAttribute('data-content');

                previewTitle.innerText = title;
                previewContent.innerText = content;
                previewWindow.style.display = 'block';
            }
        });
    });

    closeButton.addEventListener('click', function() {
        previewWindow.style.display = 'none';
    });
});
