<h2> Desafio 1 </h2>

<h4> Para poder rodar o vagrant precisamos primeiro executar o comando <em> Vagrant init </em>. 
<p>
Depois configuramos o <em> VagrantFile </em> com as devidas configurações e precisamos utilizar o comando
<em> export VAGRANT_EXPERIMENTAL="1" </em> e <em> VAGRANT_EXPERIMENTAL="disks" </em>, pois o Vagrant não consegue
atachar os discos, portanto precisamos utilizar uma versão experimental dele.
</p>
<p>
Agora é só jogar tudo para dentro da máquina virtual e dar permissão de execução (chmod +x arquivo.py), assim tudo
que estiver no arquivo python irá ser executado pelo usuário. Logo após de executar o comando nos 2 arquivos .py, assim irá instalar o java 1.8 e baixará o zeppelin em .tgz, portanto iremos descompactar e configurar o zeppelin... 
</p>

<p>
<h2> Configuração do Apache Zeppelin </h2>

<h4> Para configurar o zeppelin iremos para dentro da pasta que foi descompactada e depois para dentro do <em> conf/ </em> no diretório utilizaremos o comando mv para renomear os seguintes arquivos "zeppelin-env-.sh.template" para "zeppelin-env.sh" e "zeppelin-site.xml.template" para "zeppelin-site.xml". 
<p>

Depois alteramos o arquivo "zeppelin-site.xml", porém já está aqui o arquivo zeppelin-site.xml é só copiar e colar dentro da pasta que irá funcionar normalmente. O arquivo dar permissão o zeppelin subir para todos os IP's (0.0.0.0) e na porta 8888...
<p> Depois rodamos o comando <em> ./bin/zeppelin-daemon.sh start </em> o serviço subirá e poderemos ver na máquina host por causa da configuração do Vagrantfile.
</p>
</p>