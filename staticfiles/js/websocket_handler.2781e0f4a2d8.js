const workoutSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/workouts/'
);

workoutSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#workouts-list').innerHTML = data.message;
};

workoutSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
