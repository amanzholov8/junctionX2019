let paragraph1 = $('#id0').text()
console.log(paragraph1);
(function sayParagraph(curParagraph) {
    var form = new FormData();
    form.append('text', curParagraph);

    $.ajax({
        type: 'POST',
        url: '/narrator',
        data: form,
        processData: false,
        contentType: false,
        success: (audio) => {
            var sound = new Howl({
                src: [audio],
                autoplay: true,
                volume: 1
            });
            sound.once('load', () => {
                sound.play();
            })
        }
    });
})(paragraph1);

function startRecording() {
    var constraints = {
        audio: true,
        video: false
    }

    navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
        console.log("stream created");

        audioContext = new AudioContext();
        gumStream = stream;
        input = audioContext.createMediaStreamSource(stream);

        rec = new Recorder(input, {
            numChannels: 1
        })

        rec.record()

        console.log("The recording has started");

    }).catch(function (err) {
        console.log("Some failure occured during recording");
    });
}

function stopRecording() {
    console.log("The recording has stopped");

    rec.stop();

    //stop microphone access
    gumStream.getAudioTracks()[0].stop();

    //create the wav blob and pass it on to createDownloadLink
    rec.exportWAV(uploadToServer);
}

function uploadToServer(blob) {
    console.log('uploading');
    var fd = new FormData();
    fd.append("audio_data", blob, 'hello.wav');
    $.ajax({
        type: 'POST',
        url: '/receive_audio',
        data: fd,
        processData: false,
        contentType: false,
        success: (data) => {
            console.log('we made it');
            console.log(data);
        }
    });
}

function something() {
    startRecording();
    setTimeout(stopRecording, 3500);
}

something();