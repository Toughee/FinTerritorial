
function showData() {
	var theSelect = Spigot.Dig;
    var GDP = document.getElementById('GDP');

    GDP.innerHTML = ('You have chosen ' + theSelect[theSelect.selectedIndex].label + ',' + ' part of the ' + 
    theSelect[theSelect.selectedIndex].text + ' region.' + ' Its Industry GDP is valued in ' + 
    theSelect[theSelect.selectedIndex].value + ' billions.' + ' Its main industry is the ' + 
    theSelect[theSelect.selectedIndex].id) + ' industry';
}

