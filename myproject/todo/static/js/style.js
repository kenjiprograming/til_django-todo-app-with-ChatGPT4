// ---------- for index.html --------------------------------------------------
document.querySelectorAll('.todo-item').forEach(function(item) {
    item.addEventListener('click', function() {
        this.classList.toggle('completed');
    });
});

// ---------- for add.html --------------------------------------------------
document.querySelectorAll('.form-input').forEach(function(input) {
    input.addEventListener('input', function() {
        this.style.transform = 'scale(' + (1 + this.value.length * 0.01) + ')';
    });
});

// ---------- for delete-confirmatio.html --------------------------------------------------
document.querySelector('.delete-button-d').addEventListener('click', function(event) {
    event.preventDefault(); // Stop the form from submitting immediately
    if (confirm('Are you sure you want to delete this todo?')) {
        document.querySelector('.delete-form').submit(); // Submit the form if the user confirms deletion
    }
});
