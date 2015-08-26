# coding: utf-8
import urllib
import urllib2


texto = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Afterfest</title>
    <meta http-equiv="Content-Type"         content="text/html; charset=utf-8" /> 
    <meta content="all"                     name="robots" /> 
    <meta http-equiv="content-language"     content="portuguese" /> 
    <meta content="br"                      name="geo.country" /> 
    <meta content="true"                    name="MSSmartTagsPreventParsing" /> 
    <meta http-equiv="imagetoolbar"         content="no" /> 
    <meta content="1 days"                  name="revisit-after" /> 
    <meta content="afterfest, fotos afterfest, cobertura, cobertura afterfest, fotos balada, fotos festa, loft, areia"      name="keywords" /> 
    <meta content="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015"   name="description" /> 
    <meta property="fb:app_id" content="156248407757982"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="/css/reset.css" />
    <link rel="stylesheet" type="text/css" href="/css/site.css" />
    <link rel="stylesheet" type="text/css" href="/css/plugins.css" />
    <script type="text/javascript">
    var BASE = '';
    </script>
    
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js"></script>
    <script type="text/javascript" src="/js/jquery.fancybox-1.3.1.pack.js"></script>
    <script type="text/javascript" src="/js/jquery.jalert.packed.js"></script>
    <script type="text/javascript" src="/js/util.js"></script>
    <script type="text/javascript" src="/js/site.js"></script>
<link href="http://www.afterfest.com.br/favicon.ico" type="icon" rel="icon" /><link href="http://www.afterfest.com.br/favicon.ico" type="icon" rel="shortcut icon" />    
    
</head>
<body>

<div id="topo">
    <h1><a href="/">Afterfest</a></h1>

    <div class="ads">
        <a href="http://www.afterfest.com.br" ><img src="/uploads/banners/topo/20140212-072044-.jpg" /></a>    </div>
</div><ul id="menu">
    <li class="item">
                <a class="baladas" href="/baladas">baladas</a>
            </li><li class="item">
                <a class="bares" href="/bares">bares</a>
            </li><li class="item">
                <a class="noticias" href="/noticias">noticias</a>
            </li><li class="item">
                <a class="coberturas " href="/coberturas ">coberturas</a>
            </li><li class="item">
                <a class="agenda" href="/agenda">agenda</a>
            </li><li class="item">
                <a class="gatas" href="/gatas">gatas</a>
            </li><li class="item">
                <a class="contato" href="/contato">contatos</a>
            </li><li class="item">
                <a class="cadastro" href="/cadastro">equipe</a>
            </li></ul>
<div class="conteudo" id="galeria">
    <div class="limitador">
        
    <div class="header_pagina">
        <div class="in">
            <strong class="header_cobertura">Coberturas</strong>
            <ul>
                <li><a href="/fotos/hd/Ressaca-de-Carnaval-2015/Clube-de-Campo-Santa-Rita-SJC">ver em 3D</a></li>
            </ul>
        </div>
    </div>
    
    <div class="filtro">
        <label for="filtroLocal">LOCAL</label>            
        <select name="data[filtroLocal]" onchange="AF.buscarCoberturasPorLocal(this.value, &quot;#filtroCobertura&quot;);" id="filtroLocal">
<option value="0">TODOS</option>
<option value="16">Dunluce Irish Pub</option>
<option value="1">180° Ubatuba</option>
<option value="31">Sirena</option>
<option value="17">Parque da Cidade</option>
</select>        
        <label for="filtroCobertura">FESTA</label>            
        <select name="data[filtroCobertura]" onchange="AF.carregarCobertura(this.value);" id="filtroCobertura">
<option value="0">Escolha uma festa</option>
<option value="6-OKTOBERPUB-Banda-Chucrut's-Fernando-Meira-Bandabala-Estevao-Manfiollii">26/10/14 - 6º OKTOBERPUB - Banda Chucrut&#039;s + Fernando Meira + Bandabala + Estevão Manfiollii</option>
<option value="Loft-Club-Mogi-Inauguracao-VIP">10/04/10 - Inauguração Vip</option>
<option value="BRED-E-BRENO-Lancamento-do-novo-DVD">12/08/11 - BRED E BRENO - Lançamento do novo DVD</option>
<option value="Churas-Triplo-C">31/08/13 - Churras Itájuba</option>
<option value="Festa-a-Fantasia">21/05/11 - Festa a Fantasia</option>
<option value="Friends-on-Decks-Dai-Ferreira">20/05/11 - Friends on Decks - Dai Ferreira</option>
<option value="Loft-Club-Mogi-Inauguracao">17/04/10 - Inauguração</option>
<option value="Inauguracao-Led-Club">22/06/11 - Inauguração Led Club</option>
<option value="Just-Black-DJ-Ricardo-Menga-Robotron-63">16/04/11 - Just Black - DJ Ricardo Menga + Robotron 63</option>
<option value="KF-Hip-House-Especial-1-Ano-DJ-Puff-DJ-Milk-DJ-Hadji">19/06/13 - KF Hip House - Especial 1 Ano + B.Day Gisele Fernandes - DJ Puff + DJ Milk + DJ Hadji</option>
<option value="Lancamento-Glamour-La-Locomotive-Winter-Dj-Fadi-Alameddine">17/05/13 - Lançamento Glamour + La Locomotive Winter - Dj Fadi Alameddine</option>
<option value="Only-Vip-Dj-Rubens-Junior">22/07/11 - Only Vip - Dj Rubens Junior</option>
<option value="Ticon-Live-Pistinha-Dj-Felix">27/05/11 - Ticon Live + Pistinha Dj Felix</option>
<option value="Tribe-10-Anos">16/07/11 - Tribe 10 Anos</option>
<option value="[-Sexta-Premium-]-Caio-e-Rafael-Andre-Mello-e-Diego">20/05/11 - [ Sexta Premium ]  - Caio e Rafael + Andre Mello e Diego</option>
<option value="Aniversario-9-anos-Pub-Dom-Paulinho-The-Voice">23/10/14 - Aniversário 9 anos Pub - Dom Paulinho - The Voice</option>
<option value="Carnaval-KF-2014-Domingo-Banda-ORFEU-Grupo-Intimidade-S-A-Dj-Estevao-Manfiolli-Dj-Dogor">02/03/14 - Carnaval KF 2014 Domingo</option>
<option value="Coquetel-de-Inauguracao">15/06/11 - Coquetel de Inauguração</option>
<option value="Loft-Club-Mogi-Dj-Edgard-Fontes">24/04/10 - Dj Edgard Fontes (Anzu)</option>
<option value="Dj-Sound-Tour-2011">21/05/11 - Dj Sound Tour 2011</option>
<option value="House-of-Stage">09/04/11 - House of Stage</option>
<option value="KF-Hip-House-34-Dj-Puff">17/07/13 - KF Hip House #34 - Dj Puff</option>
<option value="Lagbeat-1-Edicao">15/10/11 - Lagbeat 1ª Edição</option>
<option value="Michel-Palazzo-Ressaca-de-carnaval">12/03/11 - Michel Palazzo - Ressaca de carnaval</option>
<option value="Sirena-Tour">23/07/11 - Sirena Tour</option>
<option value="Sirena-Tour-Vale-Edition">14/05/11 - Sirena Tour Vale Edition</option>
<option value="Spyzer-Live">20/05/11 - Spyzer Live</option>
<option value="Festa-do-Branco-Rodrigo-Faal">30/04/11 - Festa do Branco - Rodrigo Faal</option>
<option value="House-no-Deck-Elas-Convidam-Dj-Dai-Ferreira-BDay-Livia-Krom">28/09/12 - House no Deck - Elas Convidam - Dj Daï Ferreira + B.Day Lívia Krom</option>
<option value="Sirena-Sao-Paulo-Party">20/08/11 - Sirena - São Paulo Party</option>
<option value="Tom-Keller">29/07/11 - Tom Keller</option>
<option value="Top-5-Djs-Nova-Geracao">14/05/11 - Top 5 Djs - Nova Geração</option>
<option value="Veuve-Clicquot">24/09/11 - Veuve Clicquot</option>
<option value="Aniversario-do-PUB-RAIMUNDOS">05/09/13 - Aniversário do PUB - RAIMUNDOS</option>
<option value="Baile-da-Favorita">12/10/13 - Baile da Favorita</option>
<option value="ECO-Private-2-Edicao-Gabe-Luthier-Fernando-Tessis-Nuts-Noise">05/10/13 - ECO Private - 2° Edição</option>
<option value="House-no-Deck-Dj-Danilo-Stellet-Estevao-Manfiolli">27/09/13 - House no Deck - Dj Danilo Stellet + Estevão Manfiolli</option>
<option value="Octoberpub-2013">13/10/13 - Octoberpub 2013</option>
<option value="SEXTA-FEIRA">06/09/13 - SEXTA-FEIRA</option>
<option value="Camaleao-Festa-8-Anos-Hotnight">30/04/10 - Festa de 8 Anos Site Hotnight</option>
<option value="Festa-Fantasia">28/05/11 - Festa Fantasia</option>
<option value="Gabe-Live">18/03/11 - Gabe Live!</option>
<option value="Torcida-Dunlace-Irish-Pub-Brasil-Costa-do-Marfim">20/06/10 - Jogo: Brasil x Costa do Marfim</option>
<option value="Loft-Club-Mogi-Lançamento-Chandon-Baby-Disco-Rosé">29/05/10 - Lançamento Chandon Baby Disco Rosé</option>
<option value="Loft-Club-Mogi-Just-Black">22/05/10 - Just Black (Festa do Preto)</option>
<option value="Dj-Mark-Fischer-Winter-Vibe">05/06/10 - Dj Mark Fischer - Winter Vibe</option>
<option value="House-no-Deck-1309-Sexta-Feira">13/09/13 - House no Deck - 13.09 - Sexta-Feira</option>
<option value="XV-Edicao">14/09/13 - XV Edicao - FATEC</option>
<option value="Churras-e-o-Bixo-Itajuba-Parte-1">12/04/14 - Churras e o Bixo - Itajuba - Parte 1</option>
<option value="Churras-e-o-Bixo-Itajuba-Parte-2">12/04/14 - Churras e o Bixo - Itajuba - Parte 2</option>
<option value="Nud-Cabaret-Miami-Sessions-DJ-Rod-B.-e-DJ-Lance-Blaise">18/06/10 - Miami Sessions - DJ Rod B. e DJ Lance Blaise</option>
<option value="Natal-na-Mansao">25/12/10 - Natal na Mansão</option>
<option value="Carnaval-KF-2014-Sabado-Banda-ORFEU-Grupo-Intimidade-S-A-Dj-Estevao-Manfiolli-Dj-Dogor">01/03/14 - Carnaval KF 2014 Sábado</option>
<option value="Carnaval-KF-2014-Terca-Banda-ORFEU-Grupo-Intimidade-S-A-Dj-Estevao-Manfiolli-Dj-Dogor">04/03/14 - Carnaval KF 2014 Terça</option>
<option value="Chopperia-Loucos-Por-Futebol-Sextaneja-Robson-Luiz-e-Banda">09/08/13 - Chopperia Loucos Por Futebol - Sextaneja - Robson Luiz e Banda</option>
<option value="Loft-Club-Mogi-Energia-na-Loft">19/06/10 - Energia na Loft</option>
<option value="Felguk-Live">17/05/13 - Felguk Live!</option>
<option value="House-no-Deck-Festa-da-Academia-Superacao-Dj-Felipe-Faria">11/10/13 - House no Deck - Festa da Academia Superação - Dj Felipe Faria</option>
<option value="House-no-Deck-Special-BDay-Diego-Kawasaki">30/08/13 - House no Deck - Special B.Day Diego Kawasaki</option>
<option value="KF-Hip-House-36-Dj-Hadji">31/07/13 - KF Hip House #36 - Dj Hadji</option>
<option value="Neon-Party-Pub-3-Dj-Felix">21/02/14 - Neon Party Pub 3 - Dj Felix</option>
<option value="Quintas-do-Pub-Banda-Turne-Luana-Camarah">14/11/13 - Quintas do Pub - Banda Turnê Luana Camarah</option>
<option value="1-Arraia-do-PUB-Dj-Danilo-Stellet-Dj-Fabricio-Miotto-Dj-Nogue-Dj-Estevao-Manfiolli">30/06/13 - 1º Arraiá do PUB - Dj Danilo Stellet + Dj Fabrício Miotto + Dj Nogue + Dj Estevão Manfiolli</option>
<option value="Arena-dos-Loucos-Brasil-x-Alemanha-Intimidade-S-A-Eder-Saconi">08/07/14 - Arena dos Loucos - Brasil x Alemanha</option>
<option value="Arena-dos-Loucos-Brasil-x-Chile-Vee-Brondi-Intimidade-S-A-Eder-Saconi">28/06/14 - Arena dos Loucos - Brasil x Chile</option>
<option value="Arena-dos-Loucos-Brasil-x-Colombia-Dj-Danilo-Stellet-X-Fabricio-Miotto-Intimidade-S-A-Eder-Saconi">04/07/14 - Arena dos Loucos - Brasil x Colômbia</option>
<option value="Arena-dos-Loucos-Brasil-x-Mexico-Talis-Welinton-Intimidade-S-A-Eder-Saconi-DJ-Danilo-Stelett-x-Fabricio-Miotto">17/06/14 - Arena dos Loucos - Brasil x México</option>
<option value="CAPNIGHT-New-Era-Fernandinho-Beatbox-Cirilo-Claytao-Alex-Rangel-Estevao-Manfiolli-Dogor">21/11/13 - CAPNIGHT New Era - Fernandinho Beatbox + Cirilo + Claytão + Alex Rangel + Estevão Manfiolli + Dogor</option>
<option value="Carnaval-KF-2014-Sexta-Banda-ORFEU-Grupo-Intimidade-S-A-Dj-Estevao-Manfiolli-Dj-Dogor">28/02/14 - Carnaval KF 2014 Sexta</option>
<option value="Carnaval-KF-Night-Marketing-SEXTA">08/02/13 - Carnaval KF Night Marketing SEXTA</option>
<option value="Choppada-dos-Loucos-Grupo-Pode-Confiar-Eder-e-Saconi">24/08/14 - Choppada dos Loucos - Grupo Pode Confiar + Eder e Saconi</option>
<option value="Churras-da-Galera-Edicao-3-Anos">24/08/13 - Churras da Galera - Edição 3 Anos</option>
<option value="Ciroc-Party-Dj-Junior-Fonseca">07/06/13 - Ciroc Party - Dj Junior Fonseca</option>
<option value="Eclatt-Housevalley-D-NOX-Du-Serena-Tom-Keller-Andre-Pulse">17/12/11 - Eclatt Housevalley - D-NOX + Du Serena + Tom Keller + André Pulse</option>
<option value="Eco-Private">03/06/12 - Eco Private</option>
<option value="Festa-Academia-K2-DJ-Felix">19/03/14 - Festa Academia K@2 - DJ Felix</option>
<option value="Festa-de-Abertura-Temporada-2011-2012">03/09/11 - Festa de Abertura Temporada 2011/2012</option>
<option value="Forro-no-Deck-Banda-Kanavia">12/02/14 - Forró do Deck - Banda Kanaviá</option>
<option value="Grupo-Intimidade-SA-Final-Recopa-Corinthians-x-Sao-Paulo">17/07/13 - Grupo Intimidade S/A - Final Recopa - Corinthians x São Paulo</option>
<option value="House-no-Deck-Black-White-Dj-Rodrigo-S">02/05/14 - House no Deck - Black &amp; White - Dj Rodrigo S.</option>
<option value="House-no-Deck-Dj-Eduardo-Bruni">17/01/14 - House no Deck - Dj Eduardo Bruni</option>
<option value="House-no-Deck-Dj-Felipe-Faria-Dj-Noggue">09/08/13 - House no Deck - Dj Felipe Faria + Dj Noggue</option>
<option value="House-no-Deck-Dj-Paul-C-e-DJ-Oca">20/07/12 - House no Deck - Dj Paul C e DJ Oca</option>
<option value="House-no-Deck-Dj-Rubens-Jr">01/11/13 - House no Deck - Dj Rubens Jr.</option>
<option value="House-no-Deck-Edu-Zottini-2">31/01/14 - House no Deck - Edu Zottini #2</option>
<option value="House-no-Deck-Estevao-X-Dogor-BDay-Walter-Henrique">18/04/14 - House no Deck - Estevão X Dogor - B.Day Walter Henrique</option>
<option value="House-no-Deck-Lancamento-Glamour-Edicao-Mansao-Dj-Mr-Juy">08/11/13 - House no Deck - Lançamento Glamour Edição Mansão - Dj Mr. Juy</option>
<option value="House-no-Deck-Santo-Luxo-Dj-Pedro-Saab">23/08/13 - House no Deck - Santo Luxo - Dj Pedro Saab</option>
<option value="House-no-Deck-Especial-Afterfest-6-Projeto-Bassline-Andrew-Thompson">09/11/12 - House no Deck Especial Afterfest #6 - Projeto Bassline + Andrew Thompson</option>
<option value="House-Room-Vee-Brondi-Danilo-Stellet-Lucas-Brancatti">11/09/14 - House Room - Vee Brondi + Danilo Stellet + Lucas Brancatti</option>
<option value="House-Valley-Low-Sessions-Dj-Du-Serena-Dj-Pedro-Saab-Dj-Gusltavo-Alck-Dj-Edu-Reis">25/07/14 - House Valley Low Sessions - Dj Du Serena</option>
<option value="KF-12-Anos-CROSSOVER-Amon-Lima-Julio-Torres">18/12/14 - KF 12 Anos - CROSSOVER - Amon Lima + Julio Torres  +  Thainá Bertran</option>
<option value="KF-Hip-House-10-Dj-Puff-BDay-Jessica-Caroline">17/10/12 - KF Hip House #10 - Dj Puff + B.Day Jessica Caroline</option>
<option value="KF-Hip-House-28-DJ-Hadji-Anao-Live-vocal">29/05/13 - KF Hip House #28 - DJ Hadji + Anão (Live vocal)</option>
<option value="KF-Hip-House-32-DJ-Puff">26/06/13 - KF Hip House #32 - DJ Puff</option>
<option value="KF-Hip-House-37-DJ-Puff">07/08/13 - KF Hip House #37 - DJ Puff</option>
<option value="KF-Hip-House-42-Dj-Milk">25/09/13 - KF Hip House #42 - Dj Milk</option>
<option value="KF-Hip-House-45-Dj-Milk-Dj-Tom-Brasil">16/10/13 - KF Hip House #45 - Dj Milk + Dj Tom Brasil</option>
<option value="KF-Hip-House-46-Festa-da-Oakley-Dj-Hadji">23/10/13 - KF Hip House #46 - Festa da Oakley - Dj Hadji</option>
<option value="KF-Hip-House-56-DJ-Zegon-DJ-Puff-DJ-Sleep">22/01/14 - KF Hip House #56 - DJ Zegon + DJ Puff + DJ Sleep</option>
<option value="KF-Hip-House-60-Dj-Mateus-Verdelho">19/02/14 - KF Hip House #60 - COLLORZINE apresenta Dj Mateus Verdelho</option>
<option value="KF-Hip-House-61-Dj-Hadji-Dj-Sleep">12/03/14 - KF Hip House #61 - Dj Hadji + Dj Sleep</option>
<option value="KF-Hip-House-62-Dj-Jason-Salles">09/04/14 - KF Hip House #62 - Dj Jason Salles</option>
<option value="KF-Hip-House-63-Dj-Hadji-Dj-Flash">23/04/14 - KF Hip House #63 - Dj Hadji + Dj Flash</option>
<option value="KF-Hip-House-71-MIKA-Dj-Tom-Dj-Puff">02/07/14 - KF Hip House #71 - MIKA + Dj Tom + Dj Puff</option>
<option value="KF-Hip-House-74-Haikaiss-Dj-Milk">30/07/14 - KF Hip House #74 - Haikaiss + Dj Milk</option>
<option value="KF-Hip-House-Volcom-Dark-Bar-World-Tour-Dj-Puff">27/08/13 - KF Hip House - Volcom Dark Bar World Tour - Dj Puff</option>
<option value="Neon-Party-Pub-Janies-Live-Vocal">18/10/13 - Neon Party Pub - Janies Live Vocal</option>
<option value="Pagodao-do-Santo-Cupim-na-Mesa-Andre-Marinho-SP-Grupo-DIVA-Tudo-Entre-Amigos-Sambaja">25/05/13 - Pagodão do Santo - Cupim na Mesa (André Marinho - SP) + Grupo DIVA + Tudo Entre Amigos + Sambajá</option>
<option value="Pagodao-do-Santo-Cupim-na-Mesa-GPC-Batucada-E-Stefano-e-Grupo-Delirio">13/04/13 - Pagodão do Santo - Cupim na Mesa + GPC + Batucada E Stéfano e Grupo Delírio</option>
<option value="Pagodao-do-Santo-Grupo-MBM-Grupo-Pode-Confiar-Dj-Estevao-Manfiolli">12/04/14 - Pagodão do Santo 360º</option>
<option value="Pagodao-do-Villa-Grupo-Hlera">01/09/13 - Pagodão do Villa - Grupo Hlera</option>
<option value="Projeto-de-Verao-Cupim-na-Mesa-Rodolfo-Magalhaes-Danilo">19/01/14 - Projeto de Verão - Cupim na Mesa + Rodolfo Magalhães &amp; Danilo</option>
<option value="Reabertura-Dj-Estevao-Manfiolli-Dj-Dogor">07/03/14 - Reabertura - Dj Estevão Manfiolli + Dj Dogor</option>
<option value="Ressaca-de-Carnaval-Pagodao-do-Santo-Bandabala-Bateria-Mocidade-Alegre-Grupo-Pode-Confiar-Dj-Estevao-Manfiolli">15/03/14 - Ressaca de Carnaval - Pagodão do Santo</option>
<option value="St-Patrick's-Day-Dj-Estevao-Manifiolli-Dj-Dogor-Banda-Trip">16/03/14 - St. Patrick&#039;s Day - Dj Estevão Manifiolli + Dj Dogor + Banda Trip</option>
<option value="Torcida-PUB-Brasil-x-Camaroes-Bateria-da-Escola-de-Samba-VAI-VAI-BandaBala-Fernando-Meira-e-Andre-Braz-Estevao-Manfiolli-Dogor-Paul-C">23/06/14 - Torcida PUB - Brasil x Camarões</option>
<option value="Torcida-PUB-Brasil-x-Chile-Bateria-da-Escola-de-Samba-Rosas-de-Ouro-BandaBala-Fernando-Meira-e-Andre-Braz-TRIP-Estevao-Manfiolli-Dogor-Paul-C">28/06/14 - Torcida PUB - Brasil x Chile</option>
<option value="Torcida-PUB-Brasil-x-Croacia-Cupim-na-Mesa-GPC-Rodolfo-Magalhaes-e-Fernando-Meira-Estevao-Paul-C-Dogor">12/06/14 - Torcida PUB - Brasil x Croácia</option>
<option value="Torcida-PUB-Brasil-x-Mexico-Bandabala-Fernando-Meira-Estevao-Manfiolli-Dj-Dogor">17/06/14 - Torcida PUB - Brasil x México</option>
<option value="UFC-183-SILVA-x-DIAZ-no-PUB-Tiago-convida-Luana-Camarah-Giuliano-Persona-Dogor">31/01/15 - UFC 183 SILVA x DIAZ no PUB - Tiago convida Luana Camarah</option>
<option value="Ultra-Music-Festival-Brasil-Swedish-House-Mafia">03/12/11 - Ultra Music Festival - Brasil - Swedish House Mafia</option>
<option value="Warm-Up-Glamour-Dj-Noggue">20/12/13 - Warm Up Glamour - Dj Noggue</option>
<option value="[-Sexta-Premium-]-Marcos-Gustavo-Diego-Carvalho-Andre">19/08/11 - [ Sexta Premium ] - Marcos &amp; Gustavo + Diego Carvalho &amp; André</option>
<option value="House-no-Deck-Dj-Ana-Bueno">15/11/13 - House no Deck - Dj Ana Bueno</option>
<option value="Pagodao-do-Santo-Cupim-na-Mesa-Andre-Marinho-SP-Grupo-Pode-Confiar-part-Stefano-Batucada-Estevao-Manifolli">21/09/13 - Pagodão do Santo - Cupim na Mesa (André Marinho - SP) + Grupo Pode Confiar part. Stéfano + Batucada + Estevão Manifolli</option>
<option value="Pagodao-do-Santo-I-Especial-de-Natal-I-Melanina-Carioca-I-">23/12/14 - Pagodão do Santo - I - Especial de Natal  - I - Melanina Carioca</option>
<option value="House-no-Deck-Eclatt-09-Anos-Dj-Estevao-Manfiolli-BDay-Geiza-Mello">29/11/13 - House no Deck - Eclatt 09 Anos - Dj Estevão Manfiolli - B.Day Geiza Mello</option>
<option value="Camaleao-Jogo-Brasil-x-Chile">28/06/10 - Jogo: Brasil x Chile</option>
<option value="Pagodao-Do-Santo-Cupim-na-Mesa-Grupo-Pode-Confiar-Stefano-e-Grupo-Delirio-Grupo-Batucada-Dj-Estevao-Manfiolli">06/07/13 - Pagodão Do Santo - Cupim na Mesa + Grupo Pode Confiar + Stéfano e Grupo Delírio + Grupo Batucada + Dj Estevão Manfiolli</option>
<option value="Camaleao-Festa-de-1-Ano">02/07/10 - Festa de 1 Ano da Camaleão</option>
<option value="Fapija-2010-Show-Maria-Cecília-e-Rodolfo">10/07/10 - Camarote Show Maria Cecília e Rodolfo</option>
<option value="Festa-do-Branco---DEEP-Entertainment---Terraco-Daslu">28/08/10 - Festa do Branco - DEEP Entertainment - Terraço Daslu</option>
<option value="Loft-Club-Mogi-Seven-7-Pecados-Capitais">10/07/10 - Seven - 7 Pecados Capitais</option>
<option value="Fapija-2010-Thai-Estacao-Show-Maria-Cecília-e-Rodolfo">10/07/10 - Estação Show</option>
<option value="Inauguracao">04/09/10 - Inauguração - Maresias-SP</option>
<option value="Martijn-Ten-Velden">29/01/11 - Martijn Ten Velden</option>
<option value="Violive">03/09/10 - Violive</option>
<option value="We-Love-Electro-2-Anos">12/02/11 - We Love Electro - 2 Anos</option>
<option value="ElectroFolia---Dj-Dimy-Soler">31/07/10 - ElectroFolia - Dj Dimy Soler</option>
<option value="MOB-Gathering">02/10/10 - MOB Gathering - Hotel Transamérica SP</option>
<option value="Chopperia-Loucos-Por-Futebol-Sextaneja-David-Saconi">26/07/13 - Chopperia Loucos Por Futebol - Sextaneja - David Saconi</option>
<option value="Circo-Loco-The-Next-Level-Dj-Peppo-Santiago-Dj-Rodrigo-S-Legiao-Urbana-Cover">24/05/13 - Circo Loco - The Next Level - Dj Peppo Santiago + Dj Rodrigo S. + Legião Urbana Cover</option>
<option value="Desfile-OFD-10-Anos">23/09/10 - Desfile OFD 10 Anos [ Famosos ]</option>
<option value="Festa-do-Branco-ZOOM-BOXX">14/12/12 - Festa do Branco - ZOOM BOXX</option>
<option value="FourHouz-apresenta-POPOF-RDT-Downsong-Live-Three-Live-Teki-Rauzi">08/11/13 - FourHouz apresenta POPOF</option>
<option value="House-no-Deck-Encerramento-Fire-Up-Dj-Juy">02/08/13 - House no Deck - Encerramento Fire Up - Dj Juy</option>
<option value="House-no-Deck-Festa-da-Cavalera-Dj-Noggue">06/06/14 - House no Deck - Festa da Cavalera - Dj Noggue</option>
<option value="House-no-Deck-Warm-Up-Parador-Maresias-DJ-Marcelo-Tromboni">05/10/12 - House no Deck - Warm Up Parador Maresias - DJ Marcelo Tromboni</option>
<option value="House-Valley-Winter-Edition-Dj-Carka-Schwiderski-Dj-Juy-Dj-Robson-Nogueira-Dj-Thiago-Germek-Dj-Pedro-Saab">06/07/13 - House Valley Winter Edition - Dj Carla Schwiderski + Dj Juy + Dj Robson Nogueira + Dj  Thiago Germek + Dj Pedro Saab</option>
<option value="KF-Hip-House-11-Dj-Hadji">24/10/12 - KF Hip House #11 - Dj Hadji</option>
<option value="KF-Hip-House-29-DJ-Puff">05/06/13 - KF Hip House #29 - DJ Puff</option>
<option value="KF-Hip-House-44-DJ-KL-Jay-[Racionais]-BDay-Marilia-Maria">09/10/13 - KF Hip House #44 - DJ KL Jay [Racionais] + B.Day Marília Maria</option>
<option value="Neon-Party-Pub-2-Bassline">06/12/13 - Neon Party Pub 2 - Bassline</option>
<option value="Oscar-Fashion-Days">22/09/10 - Oscar Fashion Days 10 Anos</option>
<option value="Pagodao-Do-Santo-com-Cupim-na-Mesa-Intimidade-S-A-Pode-Confiar-Stefano-Dj-Estevao-Manfiolli">15/06/13 - Pagodão Do Santo com Cupim na Mesa + Intimidade S-A + Pode Confiar + Stéfano + Dj Estevão Manfiolli</option>
<option value="Soft-Open-Inauguracao-VIP">14/06/14 - Soft Open - Inauguração VIP</option>
<option value="White-Horse-Sunset-Noggue-Fabricio-Miotto-Paul-C-Dj-Dede-Silva-Estevao-Manfiolli-Giuliano-Persona-Nicodemo-Eduardo-Dias-Aerobass-Edground-Groveland">06/09/14 - White Horse Sunset - Festa Beneficente</option>
<option value="Celebration-BDay-Dj-Paul-C-Noggue-Nicodemo">26/07/13 - Celebration B.Day - Dj Paul C. + Noggue + Nicodemo</option>
<option value="Choperia-Loucos-Por-Futebol-Grupo-Pagode-Sapeca">21/07/13 - Chopperia Loucos Por Futebol - Grupo Pagode Sapeca</option>
<option value="Churras-da-Galera-Edicao-fim-de-Ano-Dj-Estevao-Manfiolli-Dj-Dogor-Dj-Edu-Reis-vs-Gustavo-Alok-Dj-Pedro-Saab-Mr-Juy-Grupo-Pode-Confiar">07/12/13 - Churras da Galera - Edição fim de Ano</option>
<option value="Farofada-do-Loucos-Talis-Wellinton-Kayera-Rafa-Carvalho-convidados">11/05/14 - Farofada do Loucos II</option>
<option value="Festa-da-Tequila-Eder-e-Saconi-Onze10-Las-Heras">26/09/14 - Festa da Tequila - Eder e Saconi + Onze10 + Las Heras</option>
<option value="Festa-de-1-Ano-da-PROMO">09/10/10 - Festa de 1 Ano da PROMO</option>
<option value="Festa-do-Branco-DJ-Andre-Plati-DJ-Lucas-Brancatti-DJ-Marcos-Conde">25/01/14 - Festa do Branco -  DJ Andre Plati + DJ Lucas Brancatti + DJ Marcos Conde</option>
<option value="Glamour-by-Fadi-Alameddine">09/03/13 - Glamour by Fadi Alameddine</option>
<option value="Grito-de-Carnaval-Samprazer-Grupo-Pode-Confiar">21/02/14 - Grito de Carnaval - Samprazer + Grupo Pode Confiar</option>
<option value="Halloween-do-Pub-Dj-Paul-C-Banda-Turne">31/10/13 - Halloween do Pub - Dj Paul C. + Banda Turnê</option>
<option value="Hedkandi-11-Years-Party-Dj-Sebastian-Arevalo-Dj-Thiago-Germek-Dj-Estevao-Manfiolli-Dj-Danilo-Stellet-Dj-Fabricio-Mioto-Dj-Pedro-Saab">20/07/13 - Hedkandi 11 Years Party - Dj Sebastian Arévalo + Dj Thiago Germek + Dj Estevão Manfiolli + Dj Danilo Stellet + Dj Fabricio Mioto + Dj Pedro Saab</option>
<option value="House-no-Deck-FUCK-YOU-PLASTIC-DJ-Bassline-Andrew-Thompson-Rose-Aloy-vs-Marcelo-Nascimento-Marcelo-Lifeguard-vs-Diego-Kaos">16/08/13 - House no Deck - !FUCK YOU PLASTIC DJ! - Bassline + Andrew Thompson + Rose Aloy vs Marcelo Nascimento + Marcelo Lifeguard vs Diego Kaos</option>
<option value="House-no-Deck-Dj-Ana-Bueno-2">11/01/14 - House no Deck - Dj Ana Bueno #2</option>
<option value="House-no-Deck-Dj-Dirceu-Pires">04/04/14 - House no Deck - Dj Dirceu Pires</option>
<option value="House-no-Deck-Dj-Marcelo-Tromboni-2">19/07/13 - House no Deck - Dj Marcelo Tromboni #2</option>
<option value="House-no-Deck-Festa-da-Ciroc-Dj-Rodrigo-S">28/03/14 - House no Deck - Festa da Ciroc - Dj Rodrigo S.</option>
<option value="House-no-Deck-House-by-Afterfest-Bassline">04/10/13 - House no Deck - House by Afterfest - Bassline</option>
<option value="House-Room-Danilo-Stellet-Pedro-Saab-Rodrigo-S">17/10/14 - House Room - Danilo Stellet + Pedro Saab + Rodrigo S.</option>
<option value="House-Valley-Magic-Edition-Dj-Robson-Nogueira-Pedro-Saab-Dogor-Estevao-Manfiolli">28/09/13 - House Valley Magic Edition - Dj Robson Nogueira + Pedro Saab +  Dogor + Estevão Manfiolli</option>
<option value="Inauguracao-Dj-Rubens-Jr">31/08/13 - Inauguração - Dj Rubens Jr.</option>
<option value="Inauguracao-Projeto-House-Room-Dj-Tom-Keller-Dj-Danilo-Stellet-Dj-David-Pires">28/08/14 - Inauguração Projeto House Room - Tom Keller + Danilo Stellet + David  Pires</option>
<option value="Indigo-Vision-Sunset-Edition-II">30/11/13 - Indigo Vision - Sunset Edition II</option>
<option value="KF-Hip-House-23-DJ-Milk">24/04/13 - KF Hip House #23 - DJ Milk - B.Day Lucas Funchal</option>
<option value="KF-Hip-House-35-DJ-Milk">24/07/13 - KF Hip House #35 - DJ Milk</option>
<option value="KF-Hip-House-43-Dj-Hadji">02/10/13 - KF Hip House #43 - Dj Hadji</option>
<option value="KF-Hip-House-47-Dj-Puff">30/10/13 - KF Hip House #47 - Dj Puff</option>
<option value="KF-Hip-House-48-Dj-Milk-Dj-Tom-Brasil">06/11/13 - KF Hip House #48 - Dj Milk + Dj Tom Brasil</option>
<option value="KF-Hip-House-53-Dj-Tom-Brasil-Dj-Milk">18/12/13 - KF Hip House #53 - Dj Tom Brasil + Dj Milk</option>
<option value="KF-Hip-House-55-Flora-Matos-Dj-Hadji">15/01/14 - KF Hip House #55 - Flora Matos + Dj Hadji - B.Day Manaíra Bachmann</option>
<option value="KF-Hip-House-57-Dj-Kalfanibanda-Pollo-Dj-Milk-Dj-Will">29/01/14 - KF Hip House #57 - Dj Kalfani(banda Pollo) + Dj Milk + Dj Will</option>
<option value="KF-Hip-House-59-Banda-Pollo-Dj-Puff">12/02/14 - KF Hip House #59 - Banda Pollo + Dj Puff</option>
<option value="KF-Hip-House-65-Leila-Moreno-Dj-Milk">07/05/14 - KF Hip House #65 - Leila Moreno + Dj Milk</option>
<option value="Pagodao-do-Santo-Pre-Carnaval-Bateria-Da-Escola-De-Samba-X-9-Paulistana-Grupo-Diva-Folia-Grupo-Pode-Confiar-Dj-Estevao-Manfiolli">22/02/14 - Pagodão do Santo - Pré Carnaval</option>
<option value="Pagodao-do-Santo-Especial-11-Anos-Cupim-na-Mesa-Andre-Marinho-SP-Grupo-DIVA-Grupo-Pode-Confiar-Estefano-Estevao-Manfiolli">02/11/13 - Pagodão do Santo Especial 11 Anos - Cupim na Mesa</option>
<option value="Warm-UP-Perfect-Life-Day-Party-Dj-Pedro-Saab-DJ-Juy-Dj-Paul-C-Dj-Estevao-Manfiolli-Dj-Felix">23/11/13 - Perfect Life Day Party - Dj Pedro Saab + DJ Juy + Dj Paul C. + Dj Estevão Manfiolli + Dj Felix</option>
<option value="Projeto-de-Verao-Banda-MBM">15/12/13 - Projeto de Verão - Banda MBM</option>
<option value="Reabertura">28/08/13 - Reabertura</option>
<option value="Ressaca-de-carnaval-Sou-Muleke-Intimidade-S-A">07/03/14 - Ressaca de carnaval - Sou Muleke + Intimidade S/A</option>
<option value="Saint-Patrick's-Day-Dj-Estevao-Manfiolli">17/03/13 - Saint Patrick&#039;s Day - Dj Estevão Manfiolli</option>
<option value="Zazueira-Pre-Carnaval-Bloco-Juca-Teles-Trovao-Brasil-e-banda-Banda-16Toneladas-Dj-Goulart">23/02/14 - Zazueira - Pré-Carnaval</option>
<option value="AfterFest-6-Anos-com-DJ-Felix-e-Renan-Noise-BDay-Suellen-Thiago-Luiz">14/09/12 - AfterFest 6 Anos com DJ Felix e Renan Noise + B.Day Suellen + Thiago + Luiz</option>
<option value="Bruno-Barudi-e-DarthVader">26/12/11 - Bruno Barudi e Darth&amp;Vader</option>
<option value="Carnaval-KF-2014-Segunda-Banda-ORFEU-Grupo-Intimidade-S-A-Dj-Estevao-Manfiolli-Dj-Dogor">03/03/14 - Carnaval KF 2014 - Segunda</option>
<option value="Ciroc-Party">15/03/13 - Cîroc Party</option>
<option value="DJ-Mario-Fischetti-Dj-Danilo-Stellet">31/08/12 - DJ Mario Fischetti + Dj Danilo Stellet</option>
<option value="Dream-Session-Dj-Andre-Plati">15/03/13 - Dream Session - Dj André Plati</option>
<option value="Golden-Christmas-Banda-A-Liga-EzEdu-Zottini-Pedro-Saab-Fabio-Casella">25/12/14 - Golden Christmas - Banda A Liga - Ez.Edu Zottini - Pedro Saab - Fabio Casella</option>
<option value="House-no-Deck-FUCK-YOU-PLASTIC-DJ-Dj-Andrew-Thompson-Dj-Marcelo-Lifeguard-e-Dj-Diego-Kaos">05/07/13 - House no Deck - !FUCK YOU PLASTIC DJ! - Dj  Andrew Thompson + Dj Marcelo Lifeguard e Dj Diego Kaos</option>
<option value="House-no-Deck-Virada-de-colecao-Colcci-Colinas-Dj-Estevao-Manfiolli">14/03/14 - House no Deck - Virada de coleção Colcci Colinas - Dj Estevão Manfiolli</option>
<option value="KF-Hip-House-26-DJ-King">15/05/13 - KF Hip House #26 - DJ King</option>
<option value="KF-Hip-House-27-DJ-Milk">22/05/13 - KF Hip House #27 - DJ Milk + B.Day Monique Bertolini</option>
<option value="KF-Hip-House-3-Dj-Milk">22/08/12 - KF Hip House #3 - Dj Milk</option>
<option value="KF-Hip-House-5-Dj-Hadji-Mc-Anao">05/09/12 - KF Hip House #5 - Dj Hadji + Mc Anão</option>
<option value="Mateus-Verdelho-KF-HIP-HOUSE">11/12/13 - Mateus Verdelho - KF HIP HOUSE</option>
<option value="One-Year-Led---White-Party">05/11/10 - One Year Led - White Party</option>
<option value="Pagodao-do-Santo-12-Anos-Melanina-Carioca-Intimidade-S-A-Estevao-Manfiolli">16/08/14 - Pagodão do Santo - 12 Anos - Melanina Carioca</option>
<option value="Pagodao-do-Santo-Especial-de-Ferias-BDay-Reber-Duarte-Cupim-na-Mesa-Andre-Marinho-Pegada-Pura-Grupo-Diva-">26/07/14 - Pagodão do Santo - Especial de Férias - B.Day Reber Duarte</option>
<option value="Quarta-e-Quinta">29/08/12 - Quarta e Quinta</option>
<option value="Rodizio-de-Quarta">01/08/12 - Rodízio de Quarta</option>
<option value="Rodizio-dos-Amigos-7">17/10/12 - Rodízio dos Amigos #7</option>
<option value="Rodizio-dos-Amigos-8">07/11/12 - Rodízio dos Amigos #8</option>
<option value="Sirena-Tour-Sao-Jose-dos-Campos-2013-Pedro-Saab-Bassline-Southmen-Tom-Keller-Press-Kit">11/05/13 - Sirena Tour São José dos Campos 2013 - Pedro Saab + Bassline + Southmen + Tom Keller + Press Kit</option>
<option value="Torcida-PUB-Brasil-x-Alemanha-Melanina-Carioca-BandaBala-Fernando-Meira-e-Andre-Braz-TRIP-Estevao-Manfiolli-Dogor-Paul-C">08/07/14 - Torcida PUB - Brasil x Alemanha - Melanina Carioca </option>
<option value="TRIBE-50-Edicao">07/07/12 - TRIBE - 50ª Edição - por Higor Bono e Walter Henrique</option>
<option value="Warm-up-Sirena-Tour-Dj-Dai-Ferreira-BDay-Bruna-Marcio-Dantas">03/05/13 - Warm-up Sirena Tour - Dj Däi Ferreira B.Day Bruna + Marcio Dantas</option>
<option value="Yazigi-apresenta-Halloween-no-PUB-Dj-Milk">31/10/12 - Yázigi apresenta Halloween no PUB - Dj Milk</option>
<option value="IM-Fest">30/10/10 - IM Fest</option>
<option value="OCTOBERPUB">24/10/10 - OCTOBERPUB</option>
<option value="After-House-Sessions-1-Edicao">04/12/11 - After House Sessions - 1º Edição</option>
<option value="Eclatt-6-anos---White-Party">06/11/10 - Eclatt 6 anos - White Party</option>
<option value="Opium-Sao-Paulo-Inauguracao">10/11/10 - Inauguração</option>
<option value="Rodizio-dos-Amigos-6">10/10/12 - Rodízio dos Amigos #6</option>
<option value="Victor-Ruiz-Any-Mello">22/02/13 - Victor Ruiz &amp; Any Mello</option>
<option value="Drods-5-Anos">13/11/10 - Drods 5 Anos</option>
<option value="Festa-da-Grife-Forum">19/11/10 - Festa da Grife Forum</option>
<option value="Glam-Friday">29/10/10 - Glam Friday</option>
<option value="IM-Fest---Electrixx">04/12/10 - IM Fest - Electrixx</option>
<option value="Reason">23/11/10 - Reason</option>
<option value="Hot-Hot---Dj-Mandraks-Le-paladino-e-Gui-Rozelli">18/12/10 - Hot Hot - Dj Mandraks, Le paladino e Gui Rozelli.</option>
<option value="D-nox--Beckers">29/12/10 - D-nox &amp; Beckers - Perfect Life</option>
<option value="Sirena-Tour-Mogi-das-Cruzes">04/08/12 - Sirena Tour Mogi das Cruzes</option>
<option value="Tequila-Night---Simone-Pellizari">17/12/10 - Tequila Night - Simone Pellizari</option>
<option value="Water-Republic-Anniversary-2010-">18/12/10 - Water Republic Anniversary 2010 </option>
<option value="Choperia-Loucos-Por-Futebol-Academia-F4-Fitness-Dj-Cristiane-selecao-">03/08/13 - Choperia Loucos Por Futebol - Academia F4 Fitness - Dj Cristiane (seleção) </option>
<option value="Choperia-Loucos-Por-Futebol-Sextaneja-2-David-Saconi">02/08/13 - Choperia Loucos Por Futebol - Sextaneja #2 - David Saconi</option>
<option value="Churras-da-Galera-Edicao-Pre-Carnaval-Anderson-Rafael-Djs-Pedro-Saab-Gustavo-Alck-Estevao-Manfiolli-Edu-Reis">22/02/14 - Churras da Galera - Edição Pré-Carnaval</option>
<option value="Deep-Aires-Sunset-Hat-Party">01/05/13 - Deep Aires - Sunset Hat Party</option>
<option value="Dunluce-Connect-Gold-Label-Reserve-Dj-Juy">29/06/13 - Dunluce Connect - Gold Label Reserve - Dj Juy</option>
<option value="House-no-Deck-Press-KIT-Sirena-">24/08/12 - House no Deck - Press KIT - Sirena </option>
<option value="Inauguracao-VIP">15/01/11 - Inauguração-VIP</option>
<option value="KF-Hip-House-22-DJ-Hadji">17/04/13 - KF Hip House #22 - DJ Hadji</option>
<option value="KF-Hip-House-24-DJ-Milk-KL-Jay">01/05/13 - KF Hip House #24 - DJ Milk + KL Jay</option>
<option value="KF-Hip-House-25-DJ-Hadji">08/05/13 - KF Hip House #25 - DJ Hadji</option>
<option value="KF-Hip-House-30-Festa-dos-Solteiros-Dj-Milk">12/06/13 - KF Hip House #30 - Festa dos Solteiros - Dj Milk</option>
<option value="B-Day-Dalton-Duarte-Dj-Carlinhos-Silva-mendigo-Marcelo-Tromboni-e-Edu-Poppo">30/06/12 - B-Day Dalton Duarte - Dj Carlinhos Silva (mendigo), Marcelo Tromboni e Edu Poppo</option>
<option value="Ballrange-Party-Special-BDay-Danilo-Stellet-Dj-Fabricio-Miotto-Noggue">18/05/13 - Ballrange Party - Special B.Day Danilo Stellet + Dj Fabricio Miotto + Noggue</option>
<option value="Bassline">16/02/13 - Bassline</option>
<option value="Carnaval-KF-Night-Marketing-TERCA">12/02/13 - Carnaval KF Night Marketing TERÇA</option>
<option value="Circus-Folia-Rodrigo-Santafe-BDay-Renato-Natali-e-Claudia-Macedo">01/02/13 - Circus Folia - Rodrigo &amp; Santafé - B.Day - Renato Natali e Claudia Macedo</option>
<option value="Comemoracao-4-Anos">17/07/13 - Comemoração 4 Anos</option>
<option value="DJ-Naccarati-Dj-Marcelo-Tromboni">01/11/12 - DJ Naccarati + Dj Marcelo Tromboni</option>
<option value="Eclatt-007-Female-Angels">13/08/11 - Eclatt 007 - Female Angels</option>
<option value="Festa-do-Branco-2011-DEEP-Entertainment-Terraco-Daslu">06/09/11 - Festa do Branco 2011 - DEEP Entertainment - Terraço Daslu</option>
<option value="House-no-Deck-Dj-Bruno-Mendez">21/09/12 - House no Deck - Dj Bruno Mendez</option>
<option value="House-no-Deck-Dj-Juy-Dj-Kleber-Alves-BDay-Dalton-Duarte-Ana-Claudia-Carvalho-Gerson-Dias">14/06/13 - House no Deck - Dj Juy + Dj Kleber Alves - B.Day Dalton Duarte + Ana Cláudia Carvalho + Gerson Dias</option>
<option value="House-no-Deck-Especial-Dia-das-Mulheres-Angel-Sun-BDay-Luiz-Gustavo">08/03/13 - House no Deck - Especial Dia das Mulheres - Angel Sun - B.Day Luiz Gustavo</option>
<option value="House-no-Deck-Warm-up-Eclatt-8-Anos">14/12/12 - House no Deck - Warm-up Eclatt 8 Anos - B.Day Grace Kelly</option>
<option value="Inauguracao-Glass-Club">22/01/11 - Inauguração Glass Club</option>
<option value="Jantar-a-la-carte">05/10/12 - Jantar a la carte</option>
<option value="Ketel-One-Cocktail's-Day">24/05/13 - Ketel One Cocktail&#039;s Day - Special B.Day Dj Carl + Kleber Alves</option>
<option value="KF-Hip-House-13-Dj-Milk">12/12/12 - KF Hip House #13 - Dj Milk</option>
<option value="KF-Hip-House-16-Dj-Milk">23/01/13 - KF Hip House #16 - Dj Milk - B.Day Bianca Rabelo =D</option>
<option value="KF-Hip-House-18-DJ-KL-Jay-DJ-Hadji">06/03/13 - KF Hip House #18 - DJ KL Jay + DJ Hadji</option>
<option value="KF-Hip-House-19-DJ-Puff">13/03/13 - KF Hip House #19 - DJ Puff</option>
<option value="KF-Hip-House-2-Dj-Hadji">15/08/12 - KF Hip House #2 -  Dj Hadji</option>
<option value="KF-Hip-House-21-DJ-CIA-DJ-Milk">10/04/13 - KF Hip House #21 - DJ CIA + DJ Milk</option>
<option value="KF-Hip-House-4-Dj-Puff">29/08/12 - KF Hip House #4 - Dj Puff</option>
<option value="KF-Hip-House-78-Pulse-011-Dj-Milk-Fernando-Meira-Estevao-Manfiolli">01/10/14 - KF Hip House #78 - Pulse 011 + Dj Milk + Fernando Meira + Estevão Manfiolli</option>
<option value="Parktronic">24/07/11 - Parktronic 2011</option>
<option value="Pre-Carnaval-Pub-Folia">27/01/13 - Pré Carnaval Pub Folia</option>
<option value="Quarta-dos-Amigos-10">19/12/12 - Quarta dos Amigos #10</option>
<option value="Quarta-dos-Amigos-12">05/03/13 - Quarta dos Amigos #12</option>
<option value="Quarta-dos-Amigos-9">12/12/12 - Quarta dos Amigos #9</option>
<option value="Reinauguracao">15/02/13 - Reinauguração</option>
<option value="Spring-Summer">23/09/12 - Spring Summer</option>
<option value="Warm-up-Electrance-6-Anos-">20/08/11 - Warm-up Electrance 6 Anos </option>
<option value="Welcome-Party-Dj-Andre-Marchezini-BDay-Aline-Zito">26/04/13 - Welcome Party - Dj André Marchezini + B.Day Aline Zito</option>
<option value="18-Anos-D-Nox-Beckers-Erick-Morillo">13/11/11 - 18 Anos D-Nox &amp; Beckers + Erick Morillo</option>
<option value="Aniversario-2-Anos-KF-Hip-House-Banda-Noizz-Dani-Castro-Estevao-Manfiolli">24/09/14 - Aniversário 2 Anos KF Hip House - Banda Noizz + Dani Castro + Estevão Manfiolli</option>
<option value="Aniversario-8-Anos-Pub-Dj-Nuts-Noise-Banda-Trip-Fernando-Meira">12/09/14 - Aniversário 8 Anos Pub - Dj Nuts Noise - Banda Trip + Fernando Meira</option>
<option value="Arena-dos-Loucos-Brasil-x-Camaroes-IntimidadeS-A-Eder-Saconi-Projeto-F3Nitro">23/06/14 - Arena dos Loucos - Brasil x Camarões</option>
<option value="Arena-dos-Loucos-Brasil-x-Croacia-Intimidade-S-A-Eder-Saconi-DJ-Tom-Keller">12/06/14 - Arena dos Loucos - Brasil x Croácia</option>
<option value="Churras-da-Galera-Edicao-4-Anos-Rafael-Augusto-Pedro-Saab-Robson-Nogueira-Gustavo-Alck-Edu-Reis-Noggue">16/08/14 - Churras da Galera Edição 4 Anos -  Rafael Augusto + DJs</option>
<option value="Deep-Aires-Dj-Andre-Marchezini">17/04/13 - Deep Aires - Dj Andre Marchezini</option>
<option value="Farofada-do-Loucos-Talis-Wellinton-Pagode-entre-Amigos-Kanavia">09/03/14 - Farofada do Loucos - Talis &amp; Wellinton + Pagode entre Amigos + Kanaviá</option>
<option value="Friday-Connect-Dj-Nuts-Noise">29/03/13 - Friday Connect - Dj Nuts Noise</option>
<option value="House-no-Deck-Bassline-Edu-Reis-BDay-Walter-Henrique-e-Felix">19/04/13 - House no Deck - Bassline + Edu Reis - B.Day Walter Henrique e Felix</option>
<option value="House-no-Deck-Dj-Edgar-Fontes">25/10/13 - House no Deck - Dj Edgar Fontes</option>
<option value="House-no-Deck-Dj-Thiago-Germek">20/09/13 - House no Deck - Dj Thiago Germek</option>
<option value="House-no-Deck-Noggue-Marco-Aoki">22/02/13 - House no Deck - Noggue + Marco Aoki</option>
<option value="House-Room-Adriano-Pagani-Danilo-Stellet-Paul-C">03/10/14 - House Room - Adriano Pagani + Danilo Stellet + Paul C.</option>
<option value="Housevalley-Dj-Vee-Brondi-Edu-Zottini-Bassline-Juy-Pedro-Saab">20/04/13 - Housevalley - Dj Vee Brondi + Edu Zottini + Bassline + Juy + Pedro Saab</option>
<option value="I'm-Free-Tonight-DJ-Fadi-Alameddine-Carla-Schwideski-Pedro-Saab-Mr-Juy-Noggue-Kleber-Alves">18/01/14 - I&#039;m Free Tonight - DJ Fadi Alameddine + Carla Schwideski</option>
<option value="KF-Hip-House-20-DJ-Hadji-Anao-live-vocal">27/03/13 - KF Hip House #20 - DJ Hadji + Anão (live vocal)</option>
<option value="KF-Hip-House-54-Dj-Milk">08/01/14 - KF Hip House #54 - Dj Milk</option>
<option value="Lancamento-Hedkandi-BDay-Allan-Mello-Dj-Rubens-Jr">28/06/13 - Lançamento Hedkandi + B.Day Allan Mello - Dj Rubens Jr.</option>
<option value="Markus-Binapfl">04/02/11 - Markus Binapfl</option>
<option value="Molhe-On-The-Road-Evento-Exclusivo-no-Brasil-DJ-DEXTRO-MC-KATORZ">21/10/11 - Molhe On The Road - Evento Exclusivo no Brasil - DJ DEXTRO + MC KATORZ</option>
<option value="Neon-Party-Pub-4-Janies-Live-Estevao-Manfiolli">27/06/14 - Neon Party Pub 4 - Janies Live + Estevão Manfiolli</option>
<option value="Oktoberfest-B-Day-Alemao-Chopperia-2-Anos">25/10/14 - Oktoberfest - B-Day Alemão Chopperia 2 Anos + B-Day Juan Pablo</option>
<option value="Pagodao-do-Santo-Pre-Carnaval-Banda-Nuwance-GPC-Estevao-Manfiolli">31/01/15 - Pagodão do Santo Pré-Carnaval - Grupo Nuwance + GPC</option>
<option value="Projeto-Buenas-Tardes-Dj-Danilo-Stellet">19/01/14 - Projeto Buenas Tardes - Dj Danilo Stellet</option>
<option value="Raul-Boesel">13/08/11 - Raul Boesel</option>
<option value="Torcida-PUB-Brasil-x-Colombia-Melanina-Carioca-BandaBala-Fernando-Meira-e-Andre-Braz-TRIP-Estevao-Manfiolli-Dogor-Paul-C">04/07/14 - Torcida PUB - Brasil x Colômbia - Melanina Carioca</option>
<option value="AfterFest-Party-7">22/03/13 - AfterFest Party #7 + B.Day Tatiana Andrade</option>
<option value="DEXTERZ">30/04/11 - DEXTERZ</option>
<option value="DJ-Tubarao">08/07/11 - DJ Tubarão</option>
<option value="Electrance-6-Anos">27/08/11 - Electrance 6 Anos</option>
<option value="House-no-Deck-1-Ano-Parceria-Daltinho-Kengao-DJ-Felix">30/11/12 - House no Deck - 1 Ano - Parceria Daltinho + Kengão - DJ Felix</option>
<option value="House-no-Deck-AfterFest-5-Edicao">27/07/12 - House no Deck - AfterFest 5ª Edição</option>
<option value="House-no-Deck-Niver-Pamela-Rodrigues-Dj-Robson-Nogueira">17/08/12 - House no Deck - Niver Pâmela Rodrigues + Dj Robson Nogueira</option>
<option value="House-no-Deck-Phyton-DJ-Oca-">26/10/12 - House no Deck - Phyton - DJ Oca </option>
<option value="House-no-Deck-TOP-DJ-Nuts-Noise-Banda-Arena-Rock">13/07/12 - House no Deck - TOP DJ Nuts Noise + Banda Arena Rock</option>
<option value="KF-Hip-House-39-Dj-Hadji">21/08/13 - KF Hip House #39 - Dj Hadji</option>
<option value="LUMIERE-Ressaca-de-Carnaval">12/03/11 - LUMIÉRE - Ressaca de Carnaval</option>
<option value="Quarta-dos-Amigos-11">27/02/13 - Quarta dos Amigos #11</option>
<option value="Rafael-Noronha">19/03/11 - Rafael Noronha</option>
<option value="Rodizio-de-Quarta-2">05/09/12 - Rodízio de Quarta #2</option>
<option value="Rodizio-de-Quarta-15-08">15/08/12 - Rodízio de Quarta - 15/08</option>
<option value="Xurras4Friends-Plinio-Guizera-e-Tail">06/11/11 - Xurras4Friends - Plínio, Guizera e Tail</option>
<option value="Dj-Vitor-Lima">05/02/11 - Dj Vitor Lima</option>
<option value="Just-White-Dj-Edgard-Fontes-Remix">12/02/11 - Just White - Dj Edgard Fontes (Remix)</option>
<option value="Temporada-2011-DJ-Mayara-Leme">28/01/11 - Abertura Temporada 2011 - DJ Mayara Leme</option>
<option value="Electrance-2011">21/05/11 - Electrance 2011</option>
<option value="Sharp-Bend-Ricardo-Menga">27/08/11 - Sharp Bend + Ricardo Menga</option>
<option value="Aniversario-7-Anos-PUB">15/09/12 - Aniversário 7 Anos PUB</option>
<option value="Camarote-AfterFest-4-Anos-Dj-Felix-Dj-Rick-DUB">14/10/11 - Camarote AfterFest  4 Anos + Dj Felix + Dj Rick DUB</option>
<option value="Eclatt-Only-White-Eletrixx-Thricie">08/10/11 - Eclatt Only White - Eletrixx + Thricie</option>
<option value="Fabio-Castro-Clube-das-Mulheres">09/07/11 - Fabio Castro</option>
<option value="House-no-Deck-DJ-Gelipe-Faria-DJ-Jr-Fonseca-Encerramento-Fire-UP">03/08/12 - House no Deck -  DJ Felipe Faria + DJ Jr. Fonseca - Encerramento Fire UP</option>
<option value="House-no-Deck-Dj-Felix-Robson-Nogueira">31/08/12 - House no Deck -Dj Felix + Robson Nogueira</option>
<option value="Imagine-Dj-Davison-Lemos">04/11/11 - Imagine - Dj Davison Lemos</option>
<option value="Just-Black-DJ-Viktor-Mora">04/11/11 - Just Black - DJ Viktor Mora</option>
<option value="KF-Hip-House-12-Dj-Hadji">07/11/12 - KF Hip House #12 - Dj Hadji</option>
<option value="KF-Hip-House-17-Negrali-DJ-Nene-DJ-Puff">20/02/13 - KF Hip House #17 - Negrali + DJ Nenê + DJ Puff</option>
<option value="KF-Hip-House-18-Dj-Milk-Groove-it">27/02/13 - KF Hip House #18 - Dj Milk + Groove It</option>
<option value="Marcelo-Sa-Pistinha-After-Renan-Noise">07/05/11 - Marcelo Sá, Pistinha After Renan Noise</option>
<option value="Rodizio-de-Quarta-3">26/09/12 - Rodízio de Quarta #3</option>
<option value="Super-Buddies-Thiago-Marques-Cassiano-E-Juliano-Urizzi-BDay-Felipe-Tavares-e-Joao-Marcelo-Andery">30/09/11 - Super Buddies - Thiago Marques, Cassiano E Juliano Urizzi B.Day Felipe Tavares e João Marcelo Andery</option>
<option value="TRIBALTECH-2012-The-End">29/09/12 - TRIBALTECH 2012 - The End - Fotógrafo: Higor Bono</option>
<option value="Warm-up-TRIBE-CLUB-Du-Serena-x-Dahan-Juy-Bassline">19/01/13 - Warm-up TRIBE CLUB - Du Serena x Dahan + Juy + Bassline</option>
<option value="[-Sexta-Premium-]-Raphael-Leandro-Bruno-Ray">26/08/11 - [ Sexta Premium ] - Raphael Leandro + Bruno &amp; Ray</option>
<option value="AfterFest-4-Anos-DJ-Feio-Felix-Rodrigo-S-e-Renan-Noise">21/10/11 - AfterFest 4 Anos - DJ Feio, Felix, Rodrigo S. e Renan Noise</option>
<option value="CABARET-|-O-Melhor-do-Funk-Carioca">07/10/11 - CABARET | O Melhor do Funk Carioca</option>
<option value="Electrixx">22/03/13 - Electrixx</option>
<option value="Heineken-Party-Night-Dj-Danilo-Stellet">21/12/13 - Heineken Party Night - Dj Danilo Stellet</option>
<option value="House-4-Friends-1">09/09/11 - House 4 Friends #1</option>
<option value="House-no-Deck-Dj-Du-Aoki-Dj-Dirceu-Pires">10/08/12 - House no Deck - Dj Du Aoki + Dj Dirceu Pires</option>
<option value="KF-Hip-House-39-Dj-Milk">14/08/13 - KF Hip House #39 - Dj Milk</option>
<option value="SPYZER">25/11/11 - SPYZER</option>
<option value="Top-Secret-2-Edicao">01/10/11 - Top Secret - 2ª Edição</option>
<option value="Bruno-Barudi-Dj-Magui">25/01/13 - Bruno Barudi + Dj Magui</option>
<option value="House-no-DECK">02/12/11 - House no DECK</option>
<option value="KF-Hip-House-Dj-Puff-Dj-Hadji">08/08/12 - KF Hip House #1 - Dj Puff + Dj Hadji</option>
<option value="KF-Hip-House-9-Dj-Milk-BDay-Marilia-Maria">10/10/12 - KF Hip House #9 - Dj Milk + B.Day Marília Maria</option>
<option value="PINK-|-HIP-HOP-|-HOUSE-">26/08/11 - PINK | HIP-HOP | HOUSE </option>
<option value="Energia-na-Glass">14/05/11 - Energia na Glass</option>
<option value="Coquetel-Freixenet-Dj-Rubens-Junior">01/03/13 - Coquetel Freixenet - Dj Rubens Junior - B.Day Sabrina Rabelo</option>
<option value="Festa-do-Branco-2011">08/10/11 - Festa do Branco 2011</option>
<option value="House-no-Deck-Dj-Robson-Nogueira-2">12/07/13 - House no Deck - Dj Robson Nogueira #2</option>
<option value="Rodizio-dos-Amigos-4">19/09/12 - Rodízio dos Amigos #4</option>
<option value="Felguk">08/12/12 - Felguk</option>
<option value="House-no-Deck-Dj-Robson-Nogueira-The-Hitmakers">19/10/12 - House no Deck - Dj Robson Nogueira - The Hitmakers</option>
<option value="KF-Hip-House-8-Dj-Hadji">26/09/12 - KF Hip House #8 - Dj Hadji</option>
<option value="Boris-Brejcha-Du-Serena">22/10/11 - Boris Brejcha + Du Serena</option>
<option value="Gallery-Classic-House">01/11/11 - Gallery Classic House - Fabiano Salles</option>
<option value="House-no-Deck-Warm-UP-Space-Ibiza-Campos-do-Jordao">06/07/12 - House no Deck - Warm UP Space Ibiza Campos do Jordão</option>
<option value="Island-Pool-Party">29/10/11 - Island Pool Party</option>
<option value="KF-Hip-House-69-Dj-Milk">18/06/14 - KF Hip House #69 - Dj Milk</option>
<option value="KF-Hip-House-7-Dj-Milk">19/09/12 - KF Hip House #7 - Dj Milk</option>
<option value="KF-Hip-House-14-Dj-Milk">19/12/12 - KF Hip House #14 - Dj Milk</option>
<option value="Gabe-Wrecked-Machines">07/01/12 - Gabe - Wrecked Machines</option>
<option value="Aniversario-do-Kengao">13/01/12 - Aniversário do Kengão</option>
<option value="Tribe-Club-Summer-Edition">21/01/12 - Tribe Club - Summer Edition</option>
<option value="KF-Hip-House-64-Dj-Hadji">30/04/14 - KF Hip House #64 - Dj Hadji</option>
<option value="La-Madre-DJ-Robson-Nogueira">27/01/12 - La Madre - DJ Robson Nogueira</option>
<option value="Summer-After">26/02/12 - Summer After</option>
<option value="Reinauguracao-Pos-Reforma">24/02/12 - Reinauguração Pós Reforma</option>
<option value="Pub-in-the-House-BDay-Sabrina-Rabelo">29/02/12 - Pub in the House + B.Day Sabrina Rabelo</option>
<option value="House-no-Deck-Dj-Nicodemo-Banda-All-Star-40">02/03/12 - House no Deck - Dj Nicodemo + Banda All Star 40</option>
<option value="House-no-Deck-Niver-Allan-Mello-Magno-Nascimento-Vanessa-Cabral">29/06/12 - House no Deck - Niver Allan Mello, Magno Nascimento, Vanessa Cabral</option>
<option value="QUARTA-FEIRA">04/09/13 - QUARTA-FEIRA</option>
<option value="House-no-Deck-com-Du-Aoki-Marco-Aoki-e-Diego-Colombini">16/03/12 - House no Deck com Du Aoki, Marco Aoki e Diego Colombini</option>
<option value="House-no-Deck-AfterFest-2a-Edicao">09/03/12 - House no Deck - AfterFest 2ª Edição + B.Day Plínio Boucault</option>
<option value="House-4-Friends-DJ-Felix-Mixer-Live">17/03/12 - House 4 Friends - DJ Felix + Mixer Live</option>
<option value="Beach-Conception-Dj-Felix-Dj-Pedro-Scarpa">24/03/12 - Beach Conception - Dj Felix + Dj Pedro Scarpa</option>
<option value="Electrance-Preview-Indoor">29/01/12 - Electrance Preview Indoor</option>
<option value="Island-Pool-Party-II">17/03/12 - Island Pool Party II</option>
<option value="House-no-Deck-com-DJ-Robson-Nogueira">23/03/12 - House no Deck com DJ Robson Nogueira</option>
<option value="House-no-Deck-Dj-Du-Aoki-Niver-Juliete-Leal">11/05/12 - House no Deck - Dj Du Aoki + Niver Juliete Leal</option>
<option value="Ministry-of-Sound-Campinas-Camarote-Perfect-Life">30/03/12 - Ministry of Sound Campinas - Camarote Perfect Life</option>
<option value="Glamour-Sao-Jose-dos-Campos">07/06/14 - Glamour - São José dos Campos</option>
<option value="House-no-Deck-AfterFest-3-Edicao-BDay-Rick-Afterfest-Dj-Felix-e-Juliana-Minini">27/04/12 - House no Deck - AfterFest 3ª Edição + B.Day Rick Afterfest, Dj Felix e Juliana Minini</option>
<option value="House-no-Deck-Niver-Danielle-Ferri-e-Maiara-Nozari-Dj-Robson-Nogueira-Dj-Marcelo-Tromboni">18/05/12 - House no Deck - Niver Danielle Ferri e Maiara Nozari - Dj Robson Nogueira, Dj Marcelo Tromboni</option>
<option value="House-no-Deck-Warm-Up-Fire-Up-Lounge-Dj-Edu-Zottini">21/06/13 - House no Deck - Warm Up Fire Up Lounge - Dj Edu Zottini</option>
<option value="Hip-House-Guten">01/06/12 - Hip-House Guten</option>
<option value="House-No-Deck-Dj-Robson-Nogueira">01/06/12 - House No Deck - Dj Robson Nogueira</option>
<option value="Intense-Aquarius">07/02/15 - Intense Aquarius</option>
<option value="KF-Hip-House-39-Dj-Mateus-Verdelho">20/11/13 - KF Hip House #49 - Dj Mateus Verdelho</option>
<option value="Carnaval-Santa-Rita-2015-Sexta-feira">19/02/15 - Carnaval Santa Rita 2015 Sexta-feira</option>
<option value="Carnaval-Santa-Rita-2015-Segunda-feira">16/02/15 - Carnaval Santa Rita 2015 - Segunda-feira</option>
<option value="Ressaca-de-Carnaval-2015" selected="selected">27/02/15 - Ressaca de Carnaval 2015</option>
<option value="Carnaval-Santa-Rita-Terca-feira-Matine">17/02/15 - Carnaval Santa Rita Terça-feira Matinê</option>
<option value="Carnaval-Santa-Rita-Terca-feira">17/02/15 - Carnaval Santa Rita Terça-feira</option>
</select>    </div>
    
    <div id="comum">
        <div class="info">
            <h2>
                                Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015            </h2>
            <div class="compartilhar">
                <div class="addthis_toolbox addthis_pill_combo">
    <a class="addthis_button_tweet" tw:count="horizontal"></a>
    <a class="addthis_button_facebook_like"></a>
    <a class="addthis_counter addthis_pill_style"></a>
</div>

<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=afterfest"></script>            </div>
        </div>
    
        <div id="listaFotos">
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78092.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 1" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78092.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 1"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 1"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78095.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 2" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78095.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 2"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 2"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78112.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 3" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78112.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 3"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 3"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78115.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 4" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78115.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 4"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 4"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78120.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 5" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78120.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 5"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 5"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78071.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 6" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78071.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 6"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 6"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78076.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 7" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78076.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 7"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 7"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78069.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 8" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78069.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 8"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 8"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78104.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 9" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78104.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 9"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 9"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78103.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 10" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78103.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 10"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 10"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78070.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 11" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78070.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 11"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 11"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78121.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 12" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78121.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 12"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 12"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78114.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 13" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78114.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 13"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 13"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78113.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 14" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78113.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 14"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 14"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78094.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 15" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78094.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 15"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 15"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78093.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 16" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78093.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 16"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 16"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78082.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 17" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78082.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 17"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 17"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78102.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 18" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78102.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 18"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 18"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78105.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 19" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78105.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 19"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 19"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78068.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 20" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78068.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 20"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 20"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78086.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 21" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78086.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 21"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 21"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78108.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 22" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78108.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 22"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 22"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78106.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 23" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78106.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 23"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 23"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78101.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 24" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78101.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 24"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 24"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78122.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 25" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78122.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 25"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 25"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78099.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 26" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78099.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 26"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 26"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78110.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 27" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78110.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 27"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 27"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78117.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 28" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78117.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 28"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 28"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78090.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 29" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78090.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 29"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 29"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78119.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 30" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78119.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 30"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 30"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78097.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 31" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78097.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 31"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 31"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78100.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 32" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78100.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 32"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 32"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78089.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 33" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78089.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 33"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 33"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78107.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 34" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78107.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 34"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 34"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78087.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 35" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78087.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 35"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 35"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78096.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 36" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78096.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 36"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 36"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78118.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 37" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78118.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 37"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 37"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78116.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 38" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78116.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 38"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 38"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78098.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 39" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78098.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 39"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 39"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78111.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 40" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78111.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 40"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 40"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78123.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 41" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78123.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 41"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 41"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78075.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 42" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78075.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 42"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 42"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78072.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 43" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78072.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 43"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 43"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78160.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 44" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78160.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 44"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 44"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78169.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 45" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78169.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 45"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 45"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78127.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 46" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78127.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 46"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 46"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78155.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 47" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78155.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 47"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 47"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78152.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 48" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78152.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 48"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 48"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78143.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 49" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78143.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 49"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 49"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78138.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 50" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78138.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 50"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 50"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78144.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 51" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78144.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 51"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 51"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78136.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 52" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78136.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 52"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 52"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78131.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 53" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78131.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 53"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 53"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78176.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 54" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78176.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 54"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 54"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78153.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 55" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78153.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 55"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 55"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78128.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 56" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78128.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 56"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 56"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78154.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 57" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78154.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 57"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 57"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78126.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 58" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78126.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 58"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 58"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78168.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 59" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78168.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 59"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 59"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78161.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 60" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78161.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 60"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 60"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78166.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 61" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78166.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 61"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 61"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78170.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 62" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78170.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 62"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 62"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78130.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 63" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78130.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 63"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 63"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78137.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 64" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78137.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 64"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 64"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78145.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 65" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78145.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 65"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 65"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78142.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 66" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78142.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 66"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 66"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78173.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 67" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78173.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 67"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 67"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78174.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 68" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78174.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 68"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 68"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78148.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 69" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78148.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 69"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 69"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78141.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 70" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78141.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 70"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 70"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78146.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 71" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78146.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 71"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 71"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78157.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 72" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78157.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 72"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 72"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78125.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 73" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78125.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 73"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 73"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78159.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 74" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78159.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 74"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 74"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78165.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 75" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78165.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 75"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 75"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78162.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 76" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78162.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 76"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 76"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78147.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 77" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78147.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 77"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 77"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78132.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 78" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78132.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 78"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 78"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78135.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 79" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78135.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 79"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 79"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78149.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 80" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78149.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 80"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 80"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78175.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 81" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78175.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 81"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 81"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78163.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 82" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78163.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 82"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 82"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78164.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 83" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78164.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 83"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 83"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78124.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 84" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78124.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 84"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 84"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78158.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 85" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78158.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 85"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 85"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78151.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 86" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78151.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 86"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 86"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78156.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 87" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78156.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 87"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 87"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78205.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 88" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78205.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 88"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 88"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78202.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 89" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78202.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 89"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 89"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78230.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 90" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78230.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 90"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 90"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78184.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 91" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78184.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 91"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 91"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78183.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 92" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78183.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 92"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 92"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78192.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 93" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78192.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 93"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 93"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78195.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 94" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78195.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 94"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 94"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78221.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 95" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78221.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 95"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 95"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78226.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 96" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78226.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 96"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 96"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78213.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 97" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78213.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 97"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 97"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78214.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 98" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78214.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 98"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 98"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78182.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 99" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78182.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 99"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 99"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78185.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 100" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78185.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 100"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 100"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78231.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 101" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78231.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 101"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 101"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78203.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 102" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78203.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 102"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 102"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78204.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 103" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78204.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 103"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 103"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78177.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 104" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78177.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 104"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 104"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78215.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 105" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78215.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 105"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 105"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78179.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 106" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78179.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 106"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 106"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78212.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 107" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78212.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 107"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 107"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78220.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 108" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78220.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 108"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 108"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78194.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 109" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78194.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 109"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 109"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78229.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 110" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78229.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 110"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 110"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78211.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 111" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78211.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 111"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 111"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78216.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 112" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78216.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 112"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 112"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78199.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 113" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78199.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 113"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 113"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78224.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 114" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78224.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 114"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 114"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78190.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 115" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78190.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 115"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 115"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78197.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 116" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78197.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 116"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 116"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78181.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 117" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78181.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 117"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 117"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78207.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 118" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78207.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 118"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 118"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78200.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 119" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78200.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 119"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 119"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78209.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 120" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78209.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 120"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 120"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78225.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 121" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78225.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 121"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 121"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78222.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 122" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78222.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 122"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 122"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78198.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 123" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78198.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 123"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 123"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78219.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 124" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78219.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 124"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 124"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78208.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 125" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78208.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 125"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 125"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78201.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 126" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78201.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 126"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 126"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78206.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 127" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78206.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 127"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 127"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78189.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 128" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78189.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 128"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 128"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78180.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 129" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78180.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 129"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 129"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78187.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 130" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78187.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 130"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 130"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78277.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 131" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78277.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 131"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 131"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78237.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 132" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78237.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 132"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 132"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78293.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 133" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78293.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 133"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 133"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78242.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 134" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78242.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 134"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 134"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78294.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 135" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78294.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 135"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 135"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78245.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 136" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78245.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 136"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 136"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78239.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 137" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78239.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 137"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 137"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78254.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 138" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78254.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 138"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 138"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78285.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 139" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78285.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 139"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 139"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78266.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 140" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78266.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 140"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 140"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78261.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 141" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78261.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 141"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 141"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78244.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 142" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78244.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 142"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 142"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78292.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 143" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78292.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 143"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 143"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78243.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 144" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78243.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 144"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 144"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78236.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 145" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78236.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 145"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 145"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78278.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 146" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78278.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 146"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 146"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78276.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 147" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78276.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 147"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 147"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78271.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 148" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78271.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 148"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 148"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78260.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 149" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78260.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 149"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 149"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78267.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 150" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78267.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 150"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 150"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78283.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 151" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78283.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 151"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 151"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78255.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 152" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78255.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 152"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 152"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78284.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 153" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78284.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 153"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 153"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78263.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 154" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78263.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 154"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 154"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78258.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 155" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78258.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 155"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 155"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78289.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 156" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78289.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 156"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 156"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78256.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 157" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78256.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 157"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 157"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78251.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 158" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78251.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 158"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 158"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78291.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 159" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78291.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 159"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 159"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78240.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 160" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78240.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 160"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 160"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78247.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 161" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78247.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 161"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 161"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78249.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 162" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78249.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 162"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 162"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78235.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 163" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78235.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 163"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 163"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78232.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 164" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78232.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 164"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 164"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78272.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 165" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78272.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 165"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 165"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78275.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 166" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78275.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 166"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 166"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78250.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 167" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78250.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 167"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 167"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78281.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 168" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78281.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 168"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 168"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78257.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 169" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78257.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 169"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 169"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78265.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 170" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78265.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 170"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 170"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78274.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 171" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78274.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 171"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 171"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78273.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 172" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78273.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 172"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 172"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78233.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 173" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78233.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 173"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 173"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78234.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 174" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78234.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 174"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 174"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78246.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 175" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78246.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 175"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 175"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78290.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 176" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78290.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 176"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 176"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78241.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 177" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78241.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 177"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 177"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78354.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 178" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78354.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 178"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 178"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78321.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 179" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78321.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 179"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 179"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78326.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 180" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78326.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 180"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 180"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78368.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 181" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78368.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 181"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 181"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78366.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 182" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78366.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 182"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 182"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78361.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 183" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78361.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 183"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 183"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78370.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 184" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78370.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 184"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 184"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78305.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 185" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78305.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 185"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 185"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78302.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 186" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78302.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 186"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 186"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78337.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 187" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78337.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 187"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 187"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78295.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 188" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78295.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 188"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 188"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78360.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 189" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78360.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 189"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 189"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78367.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 190" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78367.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 190"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 190"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78369.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 191" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78369.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 191"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 191"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78315.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 192" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78315.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 192"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 192"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78312.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 193" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78312.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 193"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 193"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78320.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 194" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78320.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 194"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 194"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78338.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 195" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78338.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 195"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 195"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78343.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 196" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78343.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 196"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 196"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78340.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 197" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78340.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 197"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 197"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78349.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 198" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78349.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 198"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 198"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78307.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 199" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78307.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 199"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 199"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78287.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 200" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78287.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 200"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 200"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78309.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 201" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78309.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 201"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 201"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78364.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 202" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78364.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 202"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 202"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78318.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 203" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78318.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 203"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 203"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78363.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 204" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78363.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 204"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 204"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78311.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 205" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78311.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 205"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 205"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78298.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 206" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78298.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 206"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 206"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78316.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 207" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78316.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 207"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 207"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78323.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 208" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78323.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 208"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 208"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78324.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 209" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78324.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 209"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 209"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78358.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 210" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78358.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 210"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 210"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78351.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 211" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78351.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 211"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 211"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78308.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 212" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78308.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 212"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 212"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78301.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 213" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78301.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 213"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 213"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78306.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 214" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78306.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 214"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 214"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78348.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 215" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78348.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 215"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 215"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78341.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 216" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78341.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 216"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 216"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78350.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 217" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78350.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 217"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 217"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78325.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 218" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78325.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 218"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 218"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78359.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 219" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78359.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 219"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 219"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78310.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 220" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78310.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 220"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 220"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78299.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 221" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78299.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 221"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 221"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78297.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 222" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78297.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 222"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 222"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78362.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 223" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78362.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 223"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 223"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78365.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 224" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78365.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 224"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 224"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78319.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 225" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78319.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 225"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 225"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78506.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 226" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78506.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 226"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 226"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78457.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 227" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78457.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 227"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 227"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78450.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 228" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78450.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 228"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 228"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78481.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 229" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78481.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 229"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 229"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78508.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 230" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78508.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 230"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 230"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78462.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 231" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78462.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 231"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 231"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78441.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 232" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78441.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 232"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 232"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78497.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 233" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78497.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 233"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 233"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78446.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 234" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78446.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 234"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 234"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78434.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 235" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78434.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 235"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 235"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78510.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 236" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78510.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 236"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 236"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78433.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 237" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78433.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 237"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 237"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78463.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 238" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78463.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 238"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 238"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78464.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 239" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78464.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 239"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 239"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78451.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 240" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78451.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 240"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 240"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78509.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 241" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78509.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 241"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 241"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78456.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 242" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78456.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 242"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 242"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78432.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 243" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78432.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 243"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 243"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78511.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 244" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78511.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 244"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 244"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78449.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 245" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78449.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 245"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 245"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78496.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 246" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78496.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 246"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 246"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78447.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 247" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78447.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 247"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 247"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78440.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 248" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78440.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 248"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 248"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78436.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 249" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78436.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 249"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 249"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78512.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 250" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78512.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 250"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 250"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78431.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 251" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78431.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 251"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 251"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78492.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 252" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78492.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 252"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 252"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78443.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 253" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78443.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 253"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 253"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78444.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 254" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78444.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 254"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 254"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78469.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 255" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78469.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 255"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 255"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78460.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 256" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78460.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 256"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 256"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78429.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 257" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78429.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 257"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 257"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78455.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 258" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78455.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 258"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 258"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78452.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 259" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78452.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 259"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 259"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78504.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 260" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78504.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 260"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 260"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78503.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 261" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78503.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 261"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 261"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78470.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 262" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78470.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 262"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 262"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78445.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 263" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78445.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 263"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 263"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78493.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 264" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78493.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 264"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 264"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78430.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 265" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78430.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 265"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 265"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78437.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 266" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78437.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 266"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 266"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78513.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 267" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78513.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 267"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 267"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78505.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 268" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78505.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 268"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 268"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78453.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 269" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78453.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 269"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 269"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78454.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 270" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78454.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 270"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 270"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78468.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 271" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78468.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 271"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 271"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78611.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 272" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78611.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 272"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 272"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78574.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 273" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78574.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 273"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 273"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78590.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 274" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78590.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 274"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 274"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78597.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 275" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78597.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 275"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 275"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78599.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 276" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78599.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 276"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 276"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78588.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 277" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78588.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 277"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 277"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78586.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 278" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78586.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 278"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 278"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78609.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 279" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78609.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 279"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 279"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78600.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 280" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78600.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 280"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 280"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78596.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 281" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78596.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 281"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 281"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78591.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 282" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78591.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 282"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 282"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78575.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 283" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78575.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 283"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 283"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78572.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 284" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78572.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 284"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 284"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78610.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 285" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78610.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 285"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 285"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78606.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 286" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78606.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 286"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 286"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78608.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 287" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78608.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 287"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 287"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78580.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 288" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78580.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 288"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 288"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78589.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 289" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78589.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 289"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 289"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78605.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 290" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78605.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 290"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 290"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78602.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 291" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78602.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 291"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 291"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78592.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 292" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78592.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 292"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 292"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78595.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 293" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78595.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 293"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 293"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78571.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 294" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78571.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 294"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 294"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78576.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 295" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78576.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 295"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 295"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78613.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 296" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78613.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 296"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 296"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78578.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 297" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78578.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 297"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 297"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78614.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 298" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78614.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 298"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 298"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78582.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 299" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78582.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 299"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 299"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78585.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 300" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78585.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 300"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 300"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78603.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 301" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78603.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 301"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 301"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78604.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 302" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78604.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 302"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 302"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78615.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 303" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78615.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 303"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 303"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78612.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 304" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78612.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 304"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 304"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78579.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 305" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78579.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 305"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 305"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78594.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 306" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78594.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 306"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 306"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78593.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 307" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78593.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 307"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 307"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78749.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 308" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78749.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 308"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 308"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78747.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 309" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78747.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 309"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 309"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78772.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 310" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78772.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 310"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 310"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78709.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 311" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78709.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 311"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 311"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78775.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 312" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78775.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 312"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 312"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78707.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 313" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78707.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 313"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 313"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78711.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 314" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78711.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 314"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 314"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78716.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 315" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78716.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 315"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 315"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78718.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 316" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78718.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 316"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 316"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78763.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 317" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78763.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 317"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 317"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78751.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 318" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78751.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 318"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 318"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78723.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 319" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78723.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 319"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 319"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78758.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 320" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78758.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 320"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 320"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78724.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 321" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78724.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 321"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 321"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78706.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 322" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78706.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 322"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 322"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78708.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 323" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78708.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 323"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 323"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78774.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 324" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78774.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 324"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 324"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78773.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 325" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78773.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 325"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 325"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78746.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 326" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78746.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 326"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 326"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78734.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 327" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78734.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 327"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 327"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78759.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 328" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78759.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 328"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 328"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78722.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 329" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78722.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 329"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 329"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78750.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 330" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78750.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 330"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 330"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78757.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 331" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78757.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 331"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 331"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78762.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 332" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78762.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 332"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 332"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78719.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 333" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78719.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 333"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 333"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78717.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 334" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78717.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 334"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 334"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78721.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 335" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78721.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 335"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 335"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78754.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 336" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78754.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 336"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 336"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78785.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 337" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78785.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 337"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 337"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78728.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 338" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78728.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 338"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 338"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78753.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 339" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78753.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 339"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 339"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78761.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 340" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78761.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 340"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 340"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78702.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 341" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78702.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 341"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 341"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78770.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 342" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78770.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 342"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 342"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78745.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 343" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78745.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 343"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 343"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78737.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 344" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78737.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 344"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 344"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78715.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 345" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78715.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 345"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 345"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78769.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 346" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78769.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 346"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 346"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78712.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 347" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78712.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 347"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 347"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78760.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 348" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78760.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 348"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 348"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78736.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 349" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78736.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 349"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 349"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78743.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 350" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78743.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 350"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 350"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78776.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 351" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78776.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 351"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 351"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78771.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 352" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78771.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 352"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 352"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78703.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 353" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78703.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 353"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 353"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78704.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 354" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78704.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 354"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 354"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78798.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 355" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78798.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 355"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 355"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78850.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 356" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78850.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 356"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 356"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78859.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 357" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78859.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 357"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 357"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78791.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 358" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78791.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 358"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 358"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78796.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 359" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78796.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 359"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 359"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78862.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 360" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78862.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 360"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 360"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78801.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 361" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78801.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 361"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 361"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78806.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 362" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78806.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 362"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 362"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78787.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 363" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78787.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 363"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 363"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78846.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 364" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78846.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 364"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 364"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78789.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 365" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78789.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 365"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 365"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78841.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 366" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78841.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 366"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 366"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78863.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 367" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78863.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 367"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 367"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78858.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 368" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78858.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 368"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 368"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78790.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 369" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78790.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 369"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 369"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78856.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 370" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78856.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 370"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 370"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78799.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 371" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78799.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 371"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 371"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78847.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 372" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78847.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 372"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 372"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78849.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 373" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78849.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 373"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 373"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78835.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 374" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78835.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 374"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 374"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78786.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 375" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78786.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 375"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 375"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78800.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 376" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78800.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 376"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 376"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78844.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 377" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78844.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 377"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 377"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78838.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 378" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78838.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 378"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 378"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78836.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 379" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78836.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 379"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 379"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78803.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 380" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78803.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 380"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 380"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78804.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 381" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78804.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 381"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 381"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78860.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 382" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78860.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 382"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 382"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78855.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 383" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78855.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 383"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 383"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78802.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 384" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78802.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 384"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 384"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78837.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 385" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78837.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 385"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 385"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78842.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 386" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78842.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 386"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 386"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78845.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 387" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78845.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 387"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 387"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78853.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 388" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78853.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 388"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 388"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78792.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 389" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78792.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 389"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 389"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78813.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 390" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78813.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 390"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 390"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78814.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 391" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78814.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 391"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 391"/></a>
                    <a href="/uploads/coberturas/Ressaca-de-Carnaval-2015/_CS78861.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 392" rel="galeria">
                <img src="/uploads/coberturas/Ressaca-de-Carnaval-2015/mini._CS78861.jpg"
                title="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 392"
                alt="Fotos Clube de Campo Santa Rita - SJC - Ressaca de Carnaval 2015 - 27/02/2015 - Foto 392"/></a>
            </div>
    <script type="text/javascript">
    $(document).ready(function(){
        $("#comum #listaFotos a").fancybox({
            autoScale: false,
            overlayOpacity: 0.9,
            overlayColor: '#000',
            padding: 0,
            margin: 0
        });
    });
    </script>
    
</div>    <br class="clear"/>
</div>

<div id="rodape">
    <div class="limitador">
        <div class="coluna">
            <img src="/img/rodape.logo.gif" />
            <br />
            <a class="block" href="mailto:contato@afterfest.com.br">contato@afterfest.com.br</a>
            <br />
            Copyright 2009 &copy; AfterFest<br />
            Todos os direitos reservados
        </div>
        <div class="coluna">
            <ul class="nav">
                                <li class="item">
                            <a class="baladas" href="/baladas">baladas</a>
                        </li><li class="item">
                            <a class="bares" href="/bares">bares</a>
                        </li><li class="item">
                            <a class="noticias" href="/noticias">noticias</a>
                        </li><li class="item">
                            <a class="coberturas " href="/coberturas ">coberturas</a>
                        </li><li class="item">
                            <a class="agenda" href="/agenda">agenda</a>
                        </li><li class="item">
                            <a class="gatas" href="/gatas">gatas</a>
                        </li><li class="item">
                            <a class="contato" href="/contato">contatos</a>
                        </li><li class="item">
                            <a class="cadastro" href="/cadastro">equipe</a>
                        </li>            </ul>
        </div>
        <div class="coluna social">
            Siga-nos no
            <a href="http://twitter.com/afterfest" target="_blank"><img src="/img/rodape.twitter.gif" /></a>
            Participe da nossa<br />
            comunidade no
            <a href="http://www.orkut.com.br/Main#Community?cmm=33229667" target="_blank"><img src="/img/rodape.orkut.gif" /></a>
        </div>
    </div>
</div><script type="text/javascript"> 
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script> 
<script type="text/javascript"> 
try {
    var pageTracker = _gat._getTracker("UA-2530999-1");
    pageTracker._trackPageview();
} catch(err) {}
</script> 
</body>
</html>
'''

import requests
import urllib2

tag = '/uploads/coberturas/Ressaca-de-Carnaval-2015/'

site = 'http://afterfest.com.br'

k = texto.find(tag)

while k != -1:
    j = k + len(tag)
    if texto[j] != 'm':  # não é thumbnail(mini)
        f = texto.find('"', j)
        nome_da_foto = texto[k + len(tag):f]
        # print (texto[k + len(tag):f])
        print nome_da_foto
        url = site + texto[k:f]
        print (url)
        # foto = requests.get(url)
        foto = urllib2.urlopen(url).read()
        tipo = type(foto)
        filef = open("C:/Users/Andreas/Desktop/afterfest/%s" % nome_da_foto, 'wb')
        #filef = open(nome_da_foto, 'wb')
        filef.write(foto)
        filef.close()
        
    k = texto.find(tag, k + 1)
    
    
