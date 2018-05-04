function showData() {
	var theSelect = Spigot.Dig;
    var GDP = document.getElementById('GDP');

    GDP.innerHTML = ('You have chosen ' + theSelect[theSelect.selectedIndex].text + '.' + "<br />"   
    + "<br />" + ' Its G.D.P is valued in $' + 
    theSelect[theSelect.selectedIndex].value + ' billion.' + "<br />" 
    + "<br />" + ' Its main industry is the ' + 
    theSelect[theSelect.selectedIndex].id) + ' industry.';
}
