function submitInfo() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    fetch('/collect-info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: name, email: email})
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('status').textContent = data;
    });
}
