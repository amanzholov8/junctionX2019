var paragraphs = $('.paragraph');
var paragraphs1 = [];
for(let i = 0; i < paragraphs.length; ++i){
    paragraphs1.push(paragraphs[i].textContent);
}
//var audios = new Array(paragraphs.length).fill(null);
var speaker = null; // Howler.js instance
var curParagraph = 0;
var isPlaying = false;

function sayParagraph(curParagraph) {
    if(curParagraph >= paragraphs.length){
        speaker = null;
        curParagraph = 0;
        isPlaying = false;
        return;
    }
    var form = new FormData();
    form.append('text', paragraphs1[curParagraph]);
    $.ajax({
        type: 'POST',
        url: '/narrator',
        data: form,
        processData: false,
        contentType: false,
        success: (audio) => {
            speaker = new Howl({
                src: [audio],
                autoplay: true,
                volume: 1
            });
            speaker.once('load', () => {
                speaker.play();
            })
            speaker.once('end', () => {
                sayParagraph(curParagraph + 1);
            });
        }
    });
}

function playStream(){
    if(!speaker)
        sayParagraph(curParagraph);
    else
        speaker.play();
}

function pauseStream(){
    if(speaker)
        speaker.pause();
}

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
        //console.log(window.current_paragraph)
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
    //console.log(window.current_paragraph);
    fd.append("audio_data", blob, 'hello.wav');
    //fd.append("paragraph", window.current_paragraph);
    //console.log(fd);
    $.ajax({
        type: 'POST',
        url: '/receive_audio',
        data: fd,
        processData: false,
        contentType: false,
        success: commandHandler
    });
}

function giveCommand() {
    startRecording();
    setTimeout(stopRecording, 3500);
}

function commandHandler(command) {
    console.log('This is the command you send me');
    //console.log(command);
    alert('The answer is: ' + command);
}

$(document).ready(function(){

});

$('#play').click(function(){
    if(!isPlaying){
        playStream();
        isPlaying = true;
    }
    else {
        pauseStream();
        isPlaying = false;
    }
});

$('#microphone').click(function(){
    giveCommand();
});