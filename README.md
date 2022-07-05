
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ╘ Sobre o desafio</a></li>
    <li><a href="#overview"> ╘ Linha do tempo</a></li>
    <li><a href="#project-folders-description"> ╘ Pastas do Projeto e decrição</a></li>
    <li><a href="#getting-started"> ╘ Rodando as aplicações localmente</a></li>

  </ol>
</details>



<!-- Sobre o desafio -->
<h2 id="about-the-project"> :pencil: Sobre o desafio</h2>

<p align="justify"> 
Obs: por favor não esqueçam de quem me recomendou foi o Pedro luiz Antonio Junior


<br>


Criar uma API que seja possível criar e utilizar uma conta virtual tendo as
seguintes funcionalidades:
<br>
○ Criar conta virtual
<br>
○ Realizar débito;
<br>
○ Realizar crédito;
<br>
○ Exibir extrato;
<br>

O sistema pode comportar ao menos 1 conta;
<br>
● Não é necessário login;
<br>
● Cada débito ou crédito deve ter uma descrição que é exibida no extrato.
<br>
● A função extrato deve exibir o saldo inicial e final do período, listando as
transações do período.
<br>
● Deve ser possível filtrar extrato apenas por crédito ou por débito.
<br>
● Deve ser disponibilizada API rest para utilizar o sistema
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Linha do tempo</h2>

<p align="justify"> 

Analisando os commits que eu fiz no repositorio ao longo do tempo <br>
é notavel que tenha começado desenvolvendo a API <br>

Como ainda não havia trabalhado profissionalmente com Django <br>
desenvolver uma api Rest do zero dentro de uma curta deadline foi um tanto desafiador <br>
entretanto usei conceitos previmente aprendidos com API s em Node para realizar as mesmas funcionalidades

Criei então uma rota para cada funcionalidade da API <br>
testes de validação para as entradas de dados

Enfrentei muitas dificuldades com as respostas do Django, acabei fazendo muitos commits de edição <br>
por fim acabei utilizando em todas as respostas returns em JSON

Após a "finalização" da API dei incio a aplicação do Front-end em Angular <br>
optei por utilizar bootstrap para criar uma interface de formularios de maneira pratica <br>
durante o desenvolvimento da interface percebi que não tinha de fato finalizado a api e alguns detalhes precisariam ser adicionados a mesma <br>

a interface ficou bem "corrida" entretanto acredito que atenda todos os requisitos, por mais que não esteja a nivel profissional de mercado <br>



</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- PROJECT FOLDERS DESCRIPTION -->
<h2 id="project-folders-description"> :floppy_disk: Project Folders Description</h2>

<ul>
  <li><b>backEnd</b> - Esta pasta foi criada pelo comando 
    <pre><code>$ django-admin startproject backEnd</code></pre>
</li>
  <li><b>front-end</b> - Esta pasta foi criada pelo comando 
<pre><code>$ ng new front-end</code></pre>
</li>

</ul>

#### - Essas duas pastas comportam as duas principais estruturas do projeto, o nome deve ser auto explicativo.

<ul>
  <li><b>backEnd/apiContaCorrente</b> - Esta pasta foi criada pelo comando 
<pre><code>$ Django-admin startapp apiContaCorrente</code></pre>
</li>
onde nela está toda a logica da nossa api, seguindo os arquivos padrões de um app Django<br>
rotas em <b> urls.py </b> <br>
testes em <b> tests.py </b>

e um arquivo adicional chamado  <b>utils.py</b> onde nele deixei os metodos das principais funcionalidades da API


</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- GETTING STARTED -->
<h2 id="getting-started"> :book: Rodando Local</h2>

<p> Para rodar a API é necessario ter instalado python no ambiente (meio obvio mas sempre bom lembrar)</p>
Entretanto para o Django funcionar corretamente é necessario clonar o mesmo do github da framework (deixei essa parte no gitIgnore, pois acredito ser similiar a um node_modules ?)<br>
<pre><code> $ git clone https://github.com/django/django.git </code></pre>

Bom com o python devidamente instalado e o django dentro do projeto, falta só instalar as dependencias<br>
navegue para dentro da api com <b> $ cd ./backEnd</b> e então installe as dependencias com:

<pre><code> $ pip install -r requirements.txt</code></pre>

Agora migrate para transformar a model em database

<pre><code> $ python manage.py migrate</code></pre>

Agora deve ser possível utilizar o comando:

<pre><code> $ python .\manage.py runserver </code></pre>

Se no terminal aparecer como abaixo está tudo certo, podemos ir para a aplicação front-end

<pre>System check identified no issues (0 silenced).
June 30, 2022 - 16:29:03
Django version 4.0.5, using settings 'backEnd.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.</pre>

Bom, agora pode abrir outro terminal, navegar até o a pasta <b> c:/.../prova-nix/front-end/ </b>
<br>
No terminal digite:
<pre><code> $ npm start</code></pre>

Se no terminal aparecer: 
<pre>> front-end@0.0.0 start
> ng serve --proxy-config proxy.config.js</pre>

Note a flag --proxy-config, se ela aparecer está inciando corretamente, se não aparecer, no terminal incie o projeto angular com:
<pre><code> $ ng serve --proxy-config proxy.config.js </code></pre>

Com tudo funcionando corretamente deve aparecer no terminal:
<pre>√ Browser application bundle generation complete.

Initial Chunk Files   | Names         |  Raw Size
vendor.js             | vendor        |   2.36 MB |
styles.css, styles.js | styles        | 411.50 kB |
polyfills.js          | polyfills     | 336.28 kB |
scripts.js            | scripts       | 145.44 kB |
main.js               | main          |  36.45 kB |
runtime.js            | runtime       |   6.85 kB |

                      | Initial Total |   3.28 MB

Build at: 2022-06-30T19:32:31.148Z - Hash: a4e59da047973ad5 - Time: 4423ms

** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **


√ Compiled successfully.</pre>


Ou similiar, Agora é só abrir o navegador e ir até o localhost:4200 e utilizar a interface que consome a API

<br>
<br>
<br>
<br>
<br>
Rovaris.
