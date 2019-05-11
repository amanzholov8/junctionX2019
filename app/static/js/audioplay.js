/* const recordAudio = () =>
    new Promise(async resolve => {
        const stream = await navigator.mediaDevices.getUserMedia({
            audio: true
        });
        const options = {
            audioBitsPerSecond : 128000,
            mimeType : 'audio/webm'
        };
        const mediaRecorder = new MediaRecorder(stream, options);
        const audioChunks = [];

        mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
        });

        const start = () => mediaRecorder.start();

        const stop = () =>
            new Promise(resolve => {
                mediaRecorder.addEventListener("stop", () => {
                    const audioBlob = new Blob(audioChunks, {type: 'audio/wav'});
                    const audioUrl = URL.createObjectURL(audioBlob);
                    const audio = new Audio(audioUrl);
                    const play = () => audio.play();
                    console.log(audioBlob);
                    resolve({
                        audioBlob,
                        audioUrl,
                        play
                    });
                });

                mediaRecorder.stop();
            });

        resolve({
            start,
            stop
        });
    });

const sleep = time => new Promise(resolve => setTimeout(resolve, time));

(async () => {
    const recorder = await recordAudio();
    recorder.start();
    await sleep(3000);
    const audio = await recorder.stop();
    audio.play();
    // audio.audioUrl
    var form = new FormData();
    form.append('audio', audio.audioBlob, 'yes.mp3');
    
    $.ajax({
        type: 'POST',
        url: '/receive_audio',
        data: form,
        processData: false,
        contentType: false,
        success: () => {
            console.log('we made it');
        }
    });
})();
*/

let paragraph1 = $('#div0').text()
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
            console.log(typeof audio);
            console.log(audio);

            var au = new Audio();  
            au.src = audio;
            //console.log(au);
            au.load();
            au.play();
            /*au.play().catch(() => {
                console.log('wtf');
            });*/
            console.log('reached');
            /*var sound = new Howl({
                src: [audio],
                autoplay: true,
                volume: 1
            })
            sound.once('load', () => {
                sound.play();
            });*/
        }
    });
})(paragraph1);