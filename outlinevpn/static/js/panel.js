function copiar(){
  var aux = document.createElement("div");
  aux.setAttribute("contentEditable", true);
  aux.innerHTML = document.getElementById("textArea").innerHTML;
  aux.setAttribute("onfocus", "document.execCommand('selectAll',false,null)"); 
  document.body.appendChild(aux);
  aux.focus();
  document.execCommand("copy");
  document.body.removeChild(aux);
  document.getElementById("copiado").style.display = "inline";
  setTimeout(function(){document.getElementById("copiado").style.display = "none";},1000);
}