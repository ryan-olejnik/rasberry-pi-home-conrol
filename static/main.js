
function setOn(gpioPin) {
	url = 'http://10.42.0.66:5000/turn_on';
	fetch(url).then(response => {
		console.log('inside fetch, response =', response);
	})
}

function setOff(gpioPin) {
        url = 'http://10.42.0.66:5000/turn_off';
        fetch(url).then(response => {
                console.log('inside fetch, response =', response);
        })
}


function toggle(gpioPin) {
        url = 'http://10.42.0.66:5000/toggle';
        fetch(url).then(response => {
                console.log('inside fetch, response =', response);
        })
}

function rave(gpioPin) {
        url = 'http://10.42.0.66:5000/toggle_rave';
        fetch(url).then(response => {
                console.log('inside fetch, response =', response);
        })
}

