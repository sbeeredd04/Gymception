// static/js/queue_websocket.js
const user = JSON.parse(document.getElementById('user_info').textContent);  // assuming you pass user info to template
const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
const ws_path = ws_scheme + '://' + window.location.host + '/ws/queue/';
const webSocket = new WebSocket(ws_path);

webSocket.onopen = function(e) {
    console.log('WebSocket Open', e);
};

webSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if(data.message === 'TIME_UP') {
        alert('Your time is up!');
        // Perform additional logic like redirecting the user
    }
};

webSocket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
};

// Function to send a message to the WebSocket
function sendMessage(message) {
    webSocket.send(JSON.stringify({
        'message': message
    }));
}
