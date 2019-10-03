function login(){
	var sen= document.getElementById('senha').value;
	if(sen!=12345){
		alert("Senha incorreta");
	}else{
		alert("Login efetuado com sucesso");
	}
}