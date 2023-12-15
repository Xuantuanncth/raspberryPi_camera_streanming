function settingTime(){
    let startTime = document.getElementById('start_time');
    let stopTime = document.getElementById('stop_time');
    if(startTime.value ==="" || stopTime.value ===""){
        alert("Please select time to start and time to stop");
    } else {
        let url = "/settingTimes/startTime="+startTime.value+"&stopTime="+stopTime.value;
        fetch(url).then((response) => {
            response.json().then((data) => {
                if (data.error) {
                    console.log("Data error: ", data.error);
                } else {
                    console.log(data);
                }
            })
        })
    }
}

function takePicture (){
    let url = "/takePicture";
    fetch(url).then((response) => {
        response.json().then((data) => {
            if (data.error) {
                console.log("Data error: ", data.error);
            } else {
                console.log(data);
            }
        })
    })
}



function settingOwner() {
    let _name = document.getElementById('i_name');
    let _email = document.getElementById('i_email');
    if((_name.value ==="")||(_email.value ==="")){
        alert("Please enter a valid email address and name.");
    } else {

        let url = "/settingOwner/name="+_name.value+"&email="+_email.value;
        fetch(url,{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }).then((response) => {
            response.json().then((data) => {
                if (data.error) {
                    console.log("Data error: ", data.error);
                } else {
                    console.log(data);
                }
            })
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}

function trainModel() {
    let url = "/trainModel";
    fetch(url).then((response) => {
        response.json().then((data) => {
            if (data.error) {
                console.log("Data error: ", data.error);
            } else {
                console.log(data);
            }
        })
    })
}