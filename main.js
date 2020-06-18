function openNav() {
    document.getElementById('mySideBar').style.width = '250px';
}

function closeNav() {
    document.getElementById('mySideBar').style.width = '0';
}

function lightSwitch() {
    document.body.classList.toggle('light-mode');
 }

 var x = 0;

 function reveal() {
     if (x==0) {
        document.getElementById('demo').classList.remove('hidden');
        x = 1;
     }
     else {
        document.getElementById('demo').classList.add('hidden');
        x = 0;
     }
 }
