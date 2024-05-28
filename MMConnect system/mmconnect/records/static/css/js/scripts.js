document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById('addRecordForm');

    form.addEventListener('submit', function(event) {
        var name = form.elements['name'].value.trim();
        var description = form.elements['description'].value.trim();

        if (!name || !description) {
            alert("Both fields are required.");
            event.preventDefault();
        }
    });
});
