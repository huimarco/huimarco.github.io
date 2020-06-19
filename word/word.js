function openNav() {
    document.getElementById('mySideBar').style.width = '250px';
}

function closeNav() {
    document.getElementById('mySideBar').style.width = '0';
}

function lightSwitch() {
    document.body.classList.toggle('light-mode');
 }

var input = document.getElementById('input');
var words = document.getElementById('wordCount');
var characters = document.getElementById('characterCount');

input.addEventListener('keyup', function(e) {
    wordCounter(e.target.value);
    characterCounter(e.target.value);
});

function isWord(str) {
    var alphaNumericFound = false;
    for (var i = 0; i < str.length; i++) {
        var code = str.charCodeAt(i);
        if ((code > 47 && code < 58) || // numeric (0-9)
            (code > 64 && code < 91) || // upper alpha (A-Z)
            (code > 96 && code < 123)) { // lower alpha (a-z)
        alphaNumericFound = true;
        return alphaNumericFound;
        }
    }
    return alphaNumericFound;
}

function wordCounter(text) {
    var text = input.value.split(' ');
    var wordCount = 0;
    for (var i = 0; i < text.length; i++) {
        if (!text[i] == ' ' && isWord(text[i])) {
        wordCount++;
        }
    }
    words.innerText = wordCount;
}

function characterCounter(text) {
    characters.innerText = text.length;
}
