
function setOn(channelName) {
	url = `http://192.168.2.59:5000/turn_on?channel=${channelName}`;
	fetch(url).then(response => {
		console.log('inside fetch, response =', response);
	})
}

function setOff(channelName) {
        url = `http://192.168.2.59:5000/turn_off?channel=${channelName}`;
        fetch(url).then(response => {
                console.log('inside fetch, response =', response);
        })
}


function toggle(channelName) {
        url = `http://192.168.2.59:5000/toggle?channel=${channelName}`;
        fetch(url).then(response => {
                console.log('inside fetch, response =', response);
        })
}


function toggleRave() {
        url = `http://192.168.2.59:5000/toggle_rave`;
        fetch(url).then(response => {
                console.log('inside fetch, response =', response);
        })
}

