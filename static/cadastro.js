function cadastro(){
	var nomeval= document.getElementById('nome').value;
	if(nomeval==""){
		alert("O campo 'nome' deve ser preenchido");
	}
	var snomeval= document.getElementById('nome').value;
	if(snomeval==""){
		alert("O campo 'sobrenome' deve ser preenchido");
	}
	
	var emailval = document.getElementById('email');
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	if (!filter.test(email.value)) {
    alert("E-mail invalido");
    email.focus;
    return false;
	}
	
	var senhaval = document.getElementById('senha').value;
	var senhaval2 = document.getElementById('senha2').value;
	if(senhaval2!=senhaval){
		alert("O campo 'confirmar senha' deve ser preenchido com a mesma senha do campo anterior");
	}else{
		return false;
	}
	
	
	
	var ida= document.getElementById('idade').value;
	if(ida<18){
		alert("Este site é destinado apenas para pessoas com mais de 18 anos de idade");
	}
}