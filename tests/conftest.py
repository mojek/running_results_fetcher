from pytest import fixture
from running_results_fetcher.runner import Runner
from running_results_fetcher.app import RunningResultFetcher
from running_results_fetcher.spider_config import SpiderConfig
from running_results_fetcher.spider import Spider


@fixture(scope="function")
def runner():
    return Runner('Michał Mojek', 1980)


@fixture(scope="function")
def rrf():
    return RunningResultFetcher('Michał Mojek', 1980)


@fixture(scope="function")
def endu_spider():
    config = SpiderConfig(domain_name='enduhub.com')
    config.runner = Runner('Michał Mojek', 1980)
    config.url_suffix = "/pl/search/?name={}&page=1".format(config.runner.name)
    Spider.set_config(config)
    return Spider


@fixture(scope="function")
def spider_config():
    runner = Runner('Michał Mojek', 1980)
    config = SpiderConfig(domain_name='enduhub.com')
    config.runner = runner
    config.url_suffix = "/pl/search/?name={}&page=1".format(runner.name)
    selctor = '.pagination .pages .active + li a::attr(href)'
    config.next_page_selector = selctor
    return config


@fixture(scope="function")
def raw_page_html():
    return """<!DOCTYPE html>








<html lang="pl">
    
    <head>
	
<title>Szukaj wyników</title>


	

	

	<link rel="stylesheet" type="text/css" href="https://static.enduhub.com/enduhub.min.css?v=r9" />
	<link rel="stylesheet" type="text/css" href="https://static.enduhub.com/rank.css?v=r5" />
        <link rel="stylesheet" type="text/css" href="https://static.enduhub.com/calendar.css?v=r5" />
	<link rel="stylesheet" type="text/css" href="https://static.enduhub.com/items.css?v=r9" />
	<link rel="stylesheet" type="text/css" href="https://static.enduhub.com/fluid.css?v=r8" />
	<link rel="stylesheet" type="text/css" media="screen" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/themes/redmond/jquery-ui.css">
	

	

	
	<meta property="og:image" content="https://static.enduhub.com/facebook-endu-logo-ludzik.png" />
	<meta property="fb:app_id" content="510812732296137" />
	

	
	<meta property="og:title" content="Enduhub - wyniki sportowe. Bieganie, triathlon, kolarstwo" />
	

	
	<meta name="title" content="Wszystkie wyniki w jednym miejscu. Wyniki bieganie - maraton, półmaraton, triathlon - ironman i olimpijski - kolarstwo - pływanie - kolarstwo górskie. Znajdź swoje wyniki !">
	
	
	<meta name="description" content="Wszystkie wyniki w jednym miejscu. Wyniki bieganie - maraton, półmaraton, triathlon - ironman i olimpijski - kolarstwo - pływanie - kolarstwo górskie. Znajdź swoje wyniki !">
	
	
	<meta name="keywords" content="wyniki sporty wytrzymałośćiowe, bieganie, kolarstwo, MTB, triatlon, pływanie, duathlon, maraton, multisport">
	

	
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	

	

<meta name="robots" content="noindex,follow">



	
	
	<link rel="canonical" href="https://enduhub.com/pl/search/"/>
	
	
    </head>
    
    
    <body>
	
	
	
	<!-- Nav bar -->
	<nav class="navbar navbar-fixed-top" role="navigation">
	    <div class="container-fluid">
		<div>
		    <a class="brand" href="/pl/"><img alt="zawody & wyniki w jednym miejscu" title="zawody & wyniki w jednym miejscu" src="https://static.enduhub.com//endupac-bar.png"></a>
		</div> 
		<div>
		    
		    
<!-- Home page does not define top bar search as it has it's own search bar -->


		    <ul class="nav navbar-nav pull-right">
			<li><a href="https://play.enduhub.com/pl/">Sklep</a></li>
			
		      <li><a href="/pl/rank/epi/">Rankingi</a></li>
			
			<li><a href="/pl/teams/wszystkie/zespo%C5%82y/">Zespoły</a></li>
			<li><a href="/pl/lista/wszystkie/imprezy/">Wszystkie zawody</a></li>
			<!--  <li><a href="/pl/zawody/kalendarz/Marzec/2019">Planuj start</a></li> -->
			<li><a href="/pl/zawody/kalendarz/2019">Kalendarz</a></li>
			<!--  <li><a href="/pl/dodaj/nowe-wyniki/">Zgłoś wyniki</a></li> -->
			<li><a href="/pl/zg%C5%82oszenia/wszystko/">Zgłoszenia</a></li>
			
			<li><a href="/pl/accounts/register/?next=/pl/search/"><i class="icon-edit icon-white"></i> Zarejestruj</a></li>
			<li><div><a class="btn btn-info dropdown-toggle" href="/pl/accounts/login/?next=/pl/search/"><i class="icon-user icon-white"></i> Zaloguj się</a></div></li>
			
		    </ul> 
		</div>
	    </div>
	</nav>		   
	<!-- End of navigation bar -->
	
	
	<!-- breadcrumbs -->
	
<ul class="breadcrumb">
    
	



<li><a href="/pl/"><img style="width:20px" src="https://static.enduhub.com/default-user-avatar.png?v=144" /></a><span class="divider">/</span></li>


	
    
    <li><a href="/pl/search/">Szukaj</a><span class="divider">/</span></li>
    
</ul>

	<!-- end of breadcrumbs block -->

	<!-- welcome -->
	
	
	<div class="alert alert-block alert-success fade in alert-welcome-box">
            <button type="button" class="close welcome-alert-button" data-dismiss="alert">Zamknij ×</button>
	    <h3 class="alert-heading">
		Witamy w enduhub ! 
	    </h3>
	    <dl class="dl-horizontal">
		<dt>
		    <img style="width:75px;vertical-align:initial"alt="enduhub" src="https://static.enduhub.com/endupac60.png"></a>
		</dt>
		<dd>
		    <b>enduhub</b> [\indu'hab, en-\].<a onclick="this.firstChild.play()"><audio src="https://static.enduhub.com/enduhub.mp3"></audio> <i class="icon-volume-up"></i></a>
		    <br/>
		    <b>endurance</b> [\in-ˈdu̇r-ən(t)s, -ˈdyu̇r-, en-\] : zdolność do długotrwałego wykonywania czynności powszechnie uważanej za trudną.
		    <br/>
		    <b>hub</b> [\ˈhəb\] : centralne i najbardziej aktywne miejsce lub element.
		</dd>
		<hr>
		<dt>
		    <img style="max-width:100px" src="https://static.enduhub.com/search-ico.png" title="Szukasz wyników po różnych stronach ?" alt="Szukasz wyników po różnych stronach ?">
		</dt>
		<dd>
		    <h3><a href="/pl/search/">Znajdź</a> swoje wyniki, sprawdź znajomych.</h3>
		    <p><a href="/pl/">http://enduhub.com</a> to wyszukiwarka wyników zawodów sportowych.Znajdziesz u nas wyniki biegów, triathlonu,kolarstwa,pływania i innych.</p>
		</dd>
		<hr>
		<dt>
		    <img style="max-width:100px" src="https://static.enduhub.com/team-ico.png" title="Szukasz wyników po różnych stronach ?" alt="Szukasz wyników po różnych stronach ?">
		</dt>
		<dd>
		    <h3><a href="/pl/accounts/register/?next=/pl/search/">Zarejestruj</a> teraz ! Dlaczego warto ? </h3>
		    <ul>
			<li> Możesz dodawać wyniki do swojej prywatnej listy. </li>
			<li> Możesz sprawdzić swój poziom na tle rówieśników - <a href="/pl/endu/help/#epi">Enduhub Performace Index.</a> </li>
			<li> Możesz zgłaszać wyniki do załadowania - <a href="/pl/dodaj/nowe-wyniki/">Zgłoś wyniki</a>. </li>
			<li> Możesz planować wynik i starty w kalendarzu - <a href="/pl/zawody/kalendarz/">Planuj</a>. </li>
			<li> Możesz założyć drużynę i zaprosić znajomych - <a href="/pl/teams/wszystkie/zespo%C5%82y/">Zespoły</a>. </li>
			<li> Stay tuned ..... ! </li>
		    </ul>
		</dd>
	    </dl>
	    <button type="button" class="btn welcome-alert-button" data-dismiss="alert"><i class="icon-off"></i> Zamknij</button>
	</div>
	
	

	
<div class="center-text">
    <h2 class="line-trough">
	<span>Szukaj</span>
    </h2>
</div>
<div>
  



<div class="search-block">
    




    <div class="enduzone_banner search_cover">
        <a rel="nofollow" target="_blank" href="/enduzone/view/79/"><img src="https://media.enduhub.com/enduzone/banner/Triathlon_Soplicowo-baner_550x190.JPG" alt="Triathlon Soplicowo" /></a>
    </div>


    <form class="form-search" action="/pl/search/" method="get">
	<fieldset>
	    <!-- <legend style="text-align:left">Wyszukaj zawodnika : </legend> -->
	    <!-- <label style="text-align:left" for="id_name">Wyszukaj zawodnika : </label> 
		 
		 Szukaj
		 -->
	    
	    
	    <div class="input-append jador">
		<input id="id_name" maxlength="200" name="name" placeholder="nazwisko albo numer startowy, np: &#39;Jan Kowalski&#39; albo &#39;666,Jan Kowalski&#39;" results="5" type="search" value="Michał Mojek" />
		<button type="submit" class="btn btn-large btn-info"><i class="icon-search icon-white"></i></button></div>	    
	</fieldset>
    </form>
</div>


  
  
  
</div>
<hr class="bluehr"/>
<hr class="bluehr"/>



<div class="muted">
  Znaleziono '27 wyników
</div>


<div>
  <form id="get_form" action="/pl/search/" method="get">
    <!--<input type='hidden' name='csrfmiddlewaretoken' value='rPIv6NU6CsVW3kKwdIbdETXA9uRtObam' /> -->
    <input id="id_name" maxlength="200" name="name" placeholder="nazwisko albo numer startowy, np: &#39;Jan Kowalski&#39; albo &#39;666,Jan Kowalski&#39;" type="hidden" value="Michał Mojek" />    
    
    <table>	   
         
      
  <thead> 
      
      <th style="text-align:center">
      
      <button onClick="return false" data-toggle="button" class="btn btn-info btn-mini" rel="help-popover" title="Filtruj" data-content="Wpisz dane w nagłówku kolumny w wciśnij filtruj. Naciśnij wyczyść aby usunąć filtr.">
	<i class="icon-question-sign icon-white"></i>
      </button>
      
      
    </th>	
    
    
    <th class="sorted column-icon orderable sortable taken user-icon" scope="col">
      <div class="sortoptions">
	<a href="?sort=taken&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle column-icon orderable sortable taken user-icon" title="Zmień"></a>
      </div>
      
      <div style="text-align:center" class="text">
	<a href="?sort=taken&amp;name=Micha%C5%82+Mojek&amp;page=1">
	  <i class="icon-edit icon-white"></i>
	</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted nr orderable sortable width-1" scope="col">
      <div class="sortoptions">
	<a href="?sort=nr&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle nr orderable sortable width-1" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=nr&amp;name=Micha%C5%82+Mojek&amp;page=1">Numer</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted orderable sortable width-1 yob" scope="col">
      <div class="sortoptions">
	<a href="?sort=yob&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle orderable sortable width-1 yob" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=yob&amp;name=Micha%C5%82+Mojek&amp;page=1">Rok</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted orderable place sortable width-1" scope="col">
      <div class="sortoptions">
	<a href="?sort=place&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle orderable place sortable width-1" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=place&amp;name=Micha%C5%82+Mojek&amp;page=1">Miejsce</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted name orderable sortable" scope="col">
      <div class="sortoptions">
	<a href="?sort=name&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle name orderable sortable" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=name&amp;name=Micha%C5%82+Mojek&amp;page=1">Zawodnik</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted best orderable sortable" scope="col">
      <div class="sortoptions">
	<a href="?sort=best&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle best orderable sortable" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=best&amp;name=Micha%C5%82+Mojek&amp;page=1">Wynik</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted event orderable sortable" scope="col">
      <div class="sortoptions">
	<a href="?sort=event&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle event orderable sortable" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=event&amp;name=Micha%C5%82+Mojek&amp;page=1">Zawody</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted distance orderable sortable" scope="col">
      <div class="sortoptions">
	<a href="?sort=distance&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle distance orderable sortable" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=distance&amp;name=Micha%C5%82+Mojek&amp;page=1">Dystans</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted orderable sortable sport" scope="col">
      <div class="sortoptions">
	<a href="?sort=sport&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle orderable sortable sport" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=sport&amp;name=Micha%C5%82+Mojek&amp;page=1">Sport</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
    
    <th class="sorted date orderable sortable width-15" scope="col">
      <div class="sortoptions">
	<a href="?sort=date&amp;name=Micha%C5%82+Mojek&amp;page=1" class="toggle date orderable sortable width-15" title="Zmień"></a>
      </div>
      
      <div class="text">
	<a href="?sort=date&amp;name=Micha%C5%82+Mojek&amp;page=1">Data</a>
      </div>
      
      <div class="clear"></div>
    </th>
    
    
  </tr>
</thead>

      
      
      
      
<tbody>	      

<tr>
  <td class="center-text">
    
    <button class="btn btn-info btn-small" type="submit" value="Filtr"><i class="icon-filter icon-white"></i> Filtruj</button>
    
  </td>
  
  <td>
    
    <div class="field_wrapper">
      
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      <input id="id_base_nr" name="base_nr" type="text" />
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      <input id="id_base_yob" name="base_yob" type="text" />
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      <input id="id_base_place" name="base_place" type="text" />
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      <select id="id_eventdistance" name="eventdistance">
<option value="" selected="selected">Wszystko</option>
<option value="19">Multi</option>
<option value="7">5 km</option>
<option value="8">10 km</option>
<option value="20">15 km</option>
<option value="2">Półmaraton</option>
<option value="1">Maraton</option>
<option value="18">1/8 Ironman</option>
<option value="17">1/4 Ironman</option>
<option value="4">1/2 Ironman</option>
<option value="5">Ironman</option>
<option value="6">Olimpijski</option>
<option value="9">0-5 km</option>
<option value="10">5-20 km</option>
<option value="11">20-50 km</option>
<option value="12">50-200 km</option>
<option value="13">Powyżej 200 km</option>
</select>
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      <select id="id_event__distance__category" name="event__distance__category">
<option value="" selected="selected">Wszystko</option>
<option value="2">Bieganie</option>
<option value="3">Pływanie</option>
<option value="4">Kolarstwo</option>
<option value="5">Triathlon</option>
<option value="6">Duathlon</option>
<option value="7">MTB</option>
<option value="8">Aquathlon</option>
<option value="9">Rolki</option>
<option value="10">Nordic Walking</option>
<option value="11">Marszobiegi</option>
<option value="12">Biegi Narciarskie</option>
<option value="13">Biegi Górskie</option>
<option value="14">Biegi Przeszkodowe</option>
</select>
      
    </div>
  </td>
  
  <td>
    
    <div class="field_wrapper">
      <input class="date-input-filter" id="id_date_0" name="date_0" type="text" />-<input class="date-input-filter" id="id_date_1" name="date_1" type="text" />
      
    </div>
  </td>
  
</tr>




<tr class='row1 Zawody'><td>#1<td class='taken'>



</td><td class='nr'>—</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
26
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/v-bieg-niepodleglosci-bieganie-10-km,jelenia-gora,2018,46429,10238072/">Mojek Michał</a></td><td class='best'>00:39:49</td><td class='event'>

<a href="/pl/wyniki/2018/11/10/bieganie/v-bieg-niepodleglosci,46429/">V Bieg Niepodległości</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2018-11-10</td></tr><tr class='row2 Zawody'><td>#2<td class='taken'>



<a href="#_blank" data-poload="/pl/results/43860/9784008/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>977</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
260
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/bieg-7-dolin-biegi-gorskie-64-km,krynica-zdroj,2018,43860,9784008/">Mojek Michał</a></td><td class='best'>10:31:35</td><td class='event'>

<a href="/pl/wyniki/2018/09/08/biegi-gorskie/bieg-7-dolin,43860/">Bieg 7 Dolin</a>

</td><td class='distance'>64 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2018-09-08</td></tr><tr class='row1 Zawody'><td>#3<td class='taken'>



</td><td class='nr'>917</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
33
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/3-x-sniezka-1-x-mont-blanc-biegi-gorskie-36-km,karpacz,2018,41470,9443091/">Mojek Michał</a></td><td class='best'>04:06:14</td><td class='event'>

<a href="/pl/wyniki/2018/06/24/biegi-gorskie/3-x-sniezka-1-x-mont-blanc,41470/">3 x Śnieżka = 1 x Mont Blanc</a>

</td><td class='distance'>36 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2018-06-24</td></tr><tr class='row2 Zawody'><td>#4<td class='taken'>



</td><td class='nr'>50</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
16
</p>
</td><td class='name'><a href="/pl/ryczkowski-daniel-mojek-michal-sulej-kamil/koncowy-wynik/sztafeta-gorska-3x20-km-biegi-gorskie-73_3-km,kudowa-zdroj,2018,38650,8904743/">Ryczkowski Daniel, Mojek Michał, Sulej Kamil</a></td><td class='best'>08:02:35</td><td class='event'>

<a href="/pl/wyniki/2018/04/07/biegi-gorskie/sztafeta-gorska-3x20-km,38650/">Sztafeta Górska 3x20+ km</a>

</td><td class='distance'>73,3 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2018-04-07</td></tr><tr class='row1 Zawody'><td>#5<td class='taken'>



<a href="#_blank" data-poload="/pl/results/34655/8275743/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>367</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
46
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/iv-bieg-niepodleglosci-bieganie-10-km,jelenia-gora,2017,34655,8275743/">Mojek Michał</a></td><td class='best'>00:41:20</td><td class='event'>

<a href="/pl/wyniki/2017/11/11/bieganie/iv-bieg-niepodleglosci,34655/">IV Bieg Niepodległości</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2017-11-11</td></tr><tr class='row2 Zawody'><td>#6<td class='taken'>



<a href="#_blank" data-poload="/pl/results/32792/7852440/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>16535</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
2428
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/39-pzu-maraton-warszawski-bieganie-maraton,warszawa,2017,32792,7852440/">Mojek Michał</a></td><td class='best'>03:59:43</td><td class='event'>

<a href="/pl/wyniki/2017/09/24/bieganie/39-pzu-maraton-warszawski,32792/">39. PZU Maraton Warszawski</a>

</td><td class='distance'>Maraton</td><td class='sport'>Bieganie</td><td class='date'>2017-09-24</td></tr><tr class='row1 Zawody'><td>#7<td class='taken'>



<a href="#_blank" data-poload="/pl/results/30038/7310707/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>548</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
26
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/3-x-sniezka-1-x-mont-blanc-biegi-gorskie-36-km,karpacz,2017,30038,7310707/">Mojek Michał</a></td><td class='best'>04:19:11</td><td class='event'>

<a href="/pl/wyniki/2017/06/24/biegi-gorskie/3-x-sniezka-1-x-mont-blanc,30038/">3 x Śnieżka = 1 x Mont Blanc </a>

</td><td class='distance'>36 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2017-06-24</td></tr><tr class='row2 Zawody'><td>#8<td class='taken'>



<a href="#_blank" data-poload="/pl/results/29716/7272654/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>3341</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
312
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/vi-rzezniczek-biegi-gorskie-28-km,cisna,2017,29716,7272654/">Mojek Michał</a></td><td class='best'>04:34:19</td><td class='event'>

<a href="/pl/wyniki/2017/06/17/biegi-gorskie/vi-rzezniczek,29716/">VI Rzeźniczek</a>

</td><td class='distance'>28 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2017-06-17</td></tr><tr class='row1 Zawody'><td>#9<td class='taken'>



<a href="#_blank" data-poload="/pl/results/29004/7155616/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>177</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
59
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/chojnik-karkonoski-festiwal-biegowy-biegi-gorskie-46-km,jelenia-gora,2017,29004,7155616/">Mojek Michał</a></td><td class='best'>05:49:17</td><td class='event'>

<a href="/pl/wyniki/2017/05/27/biegi-gorskie/chojnik-karkonoski-festiwal-biegowy,29004/">Chojnik Karkonoski Festiwal Biegowy</a>

</td><td class='distance'>46 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2017-05-27</td></tr><tr class='row2 Zawody'><td>#10<td class='taken'>



<a href="#_blank" data-poload="/pl/results/28364/6932856/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>124</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
21
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/xxvi-memorial-uliczny-im-michala-fludra-bieganie-10-km,wlen,2017,28364,6932856/">Mojek Michał</a></td><td class='best'>00:41:11</td><td class='event'>

<a href="/pl/wyniki/2017/05/07/bieganie/xxvi-memorial-uliczny-im-michala-fludra,28364/">XXVI Memoriał Uliczny im. Michała Fludra</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2017-05-07</td></tr><tr class='row1 Zawody'><td>#11<td class='taken'>



<a href="#_blank" data-poload="/pl/results/27316/6718985/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>786</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
52
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/bieg-bitwy-pod-legnica-1241-polmaraton-bieganie-polmaraton,legnica,2017,27316,6718985/">Mojek Michał</a></td><td class='best'>01:32:43</td><td class='event'>

<a href="/pl/wyniki/2017/04/09/bieganie/bieg-bitwy-pod-legnica-1241-polmaraton,27316/">Bieg “Bitwy Pod Legnicą 1241 - Półmaraton”</a>

</td><td class='distance'>Półmaraton</td><td class='sport'>Bieganie</td><td class='date'>2017-04-09</td></tr><tr class='row2 Zawody'><td>#12<td class='taken'>



<a href="#_blank" data-poload="/pl/results/26581/6579907/popover/athlete/michal-mojek/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>210</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
61
</p>
</td><td class='name'><a href="/pl/michal-mojek/koncowy-wynik/iv-zimowy-ultramaraton-karkonoski-im-tomka-kowalskiego-biegi-gorskie-53-km,karpacz,2017,26581,6579907/">Michał Mojek</a></td><td class='best'>06:47:10</td><td class='event'>

<a href="/pl/wyniki/2017/03/11/biegi-gorskie/iv-zimowy-ultramaraton-karkonoski-im-tomka-kowalskiego,26581/">IV Zimowy Ultramaraton Karkonoski im. Tomka Kowalskiego</a>

</td><td class='distance'>53 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2017-03-11</td></tr><tr class='row1 Zawody'><td>#13<td class='taken'>



<a href="#_blank" data-poload="/pl/results/23944/6278904/popover/athlete/michal-mojek/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>134</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
12
</p>
</td><td class='name'><a href="/pl/michal-mojek/koncowy-wynik/ultrakotlina-70-mezczyzni-biegi-gorskie-78_3-km,janowice-wielkie-jakuszyce,2016,23944,6278904/">Michał Mojek</a></td><td class='best'>—</td><td class='event'>

<a href="/pl/wyniki/2016/10/15/biegi-gorskie/ultrakotlina-70-mezczyzni,23944/">Ultrakotlina 70 - Mężczyźni</a>

</td><td class='distance'>78,3 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2016-10-15</td></tr><tr class='row2 Zawody'><td>#14<td class='taken'>



<a href="#_blank" data-poload="/pl/results/22904/6089927/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>1559</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
202
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/iii-cwiercultramaraton-bieszczadzki-biegi-gorskie-13-km,cisna,2016,22904,6089927/">Mojek Michał</a></td><td class='best'>02:32:19</td><td class='event'>

<a href="/pl/wyniki/2016/10/09/biegi-gorskie/iii-cwiercultramaraton-bieszczadzki,22904/">III Ćwierćultramaraton Bieszczadzki</a>

</td><td class='distance'>13 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2016-10-09</td></tr><tr class='row1 Zawody'><td>#15<td class='taken'>



<a href="#_blank" data-poload="/pl/results/21310/5728387/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>2493</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
1775
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/iii-bmw-polmaraton-praski-bieganie-polmaraton,warszawa,2016,21310,5728387/">Mojek Michał</a></td><td class='best'>01:54:59</td><td class='event'>

<a href="/pl/wyniki/2016/08/28/bieganie/iii-bmw-polmaraton-praski,21310/">III BMW Półmaraton Praski</a>

</td><td class='distance'>Półmaraton</td><td class='sport'>Bieganie</td><td class='date'>2016-08-28</td></tr><tr class='row2 Zawody'><td>#16<td class='taken'>



<a href="#_blank" data-poload="/pl/results/19516/5436365/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>450</td><td class='yob'>—</td><td class='place'>










<p class="centered-text">
28
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/3-x-sniezka-1-x-mont-blanc-sredni-biegi-gorskie-33-km,karpacz,2016,19516,5436365/">Mojek Michał</a></td><td class='best'>05:00:03</td><td class='event'>

<a href="/pl/wyniki/2016/06/25/biegi-gorskie/3-x-sniezka-1-x-mont-blanc-sredni,19516/">3 x Śnieżka = 1 x Mont Blanc - Średni</a>

</td><td class='distance'>33 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2016-06-25</td></tr><tr class='row1 Zawody'><td>#17<td class='taken'>



<a href="#_blank" data-poload="/pl/results/16329/4754477/popover/athlete/michal-mojek/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>185</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
226
</p>
</td><td class='name'><a href="/pl/michal-mojek/koncowy-wynik/iii-zimowy-ultramaraton-karkonoski-im-tomka-kowalskiego-biegi-gorskie-53-km,karpacz,2016,16329,4754477/">Michał Mojek</a></td><td class='best'>10:03:05</td><td class='event'>

<a href="/pl/wyniki/2016/03/12/biegi-gorskie/iii-zimowy-ultramaraton-karkonoski-im-tomka-kowalskiego,16329/">III Zimowy Ultramaraton Karkonoski im. Tomka Kowalskiego</a>

</td><td class='distance'>53 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2016-03-12</td></tr><tr class='row2 Zawody'><td>#18<td class='taken'>



<a href="#_blank" data-poload="/pl/results/13564/4330146/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>234</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
80
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/2-bieg-niepodleglosci-bieganie-10-km,jelenia-gora,2015,13564,4330146/">Mojek Michał</a></td><td class='best'>00:44:11</td><td class='event'>

<a href="/pl/wyniki/2015/11/11/bieganie/2-bieg-niepodleglosci,13564/">2 Bieg Niepodległości</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2015-11-11</td></tr><tr class='row1 Zawody'><td>#19<td class='taken'>



<a href="#_blank" data-poload="/pl/results/12763/4172677/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>3903</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
1747
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/16-poznan-maraton-bieganie-maraton,poznan,2015,12763,4172677/">Mojek Michał</a></td><td class='best'>03:41:32</td><td class='event'>

<a href="/pl/wyniki/2015/10/11/bieganie/16-poznan-maraton,12763/">16. Poznań Maraton</a>

</td><td class='distance'>Maraton</td><td class='sport'>Bieganie</td><td class='date'>2015-10-11</td></tr><tr class='row2 Zawody'><td>#20<td class='taken'>



<a href="#_blank" data-poload="/pl/results/12513/4125116/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>629</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
3714
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/biegnij-warszawo-bieganie-10-km,warszawa,2015,12513,4125116/">Mojek Michał</a></td><td class='best'>00:58:20</td><td class='event'>

<a href="/pl/wyniki/2015/10/04/bieganie/biegnij-warszawo,12513/">Biegnij Warszawo</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2015-10-04</td></tr><tr class='row1 Zawody'><td>#21<td class='taken'>



<a href="#_blank" data-poload="/pl/results/11409/3937400/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>1419</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
3398
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/2-bmw-polmaraton-praski-bieganie-polmaraton,warszawa,2015,11409,3937400/">Mojek Michał</a></td><td class='best'>02:10:06</td><td class='event'>

<a href="/pl/wyniki/2015/08/30/bieganie/2-bmw-polmaraton-praski,11409/">2. BMW Półmaraton Praski</a>

</td><td class='distance'>Półmaraton</td><td class='sport'>Bieganie</td><td class='date'>2015-08-30</td></tr><tr class='row2 Zawody'><td>#22<td class='taken'>



<a href="#_blank" data-poload="/pl/results/11321/3917824/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>26</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
114
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/jakuszycki-polmaraton-bieganie-22-km,jakuszyce,2015,11321,3917824/">Mojek Michał</a></td><td class='best'>01:59:34</td><td class='event'>

<a href="/pl/wyniki/2015/08/29/bieganie/jakuszycki-polmaraton,11321/">Jakuszycki Półmaraton</a>

</td><td class='distance'>22 km</td><td class='sport'>Bieganie</td><td class='date'>2015-08-29</td></tr><tr class='row1 Zawody'><td>#23<td class='taken'>



<a href="#_blank" data-poload="/pl/results/11417/3939842/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>26</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
115
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/letni-bieg-piastow-jakuszycki-polmaraton-biegi-gorskie-22-km,jakuszyce,2015,11417,3939842/">Mojek Michał</a></td><td class='best'>01:59:34</td><td class='event'>

<a href="/pl/wyniki/2015/08/29/biegi-gorskie/letni-bieg-piastow-jakuszycki-polmaraton,11417/">Letni Bieg Piastów - Jakuszycki Półmaraton</a>

</td><td class='distance'>22 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2015-08-29</td></tr><tr class='row2 Zawody'><td>#24<td class='taken'>



<a href="#_blank" data-poload="/pl/results/9663/3701830/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>474</td><td class='yob'>1980</td><td class='place'>










<p class="centered-text">
47
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/3-x-sniezka-1-x-mont-blanc-ultra-bieganie-57-km,karpacz,2015,9663,3701830/">Mojek Michał</a></td><td class='best'>08:59:32</td><td class='event'>

<a href="/pl/wyniki/2015/07/04/bieganie/3-x-sniezka-1-x-mont-blanc-ultra,9663/">3 x Śnieżka = 1 x Mont Blanc  - ULTRA</a>

</td><td class='distance'>57 km</td><td class='sport'>Bieganie</td><td class='date'>2015-07-04</td></tr><tr class='row1 Zawody'><td>#25<td class='taken'>



<a href="#_blank" data-poload="/pl/results/3879/2619562/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>264</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
78
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/bieg-niepodleglosci-bieganie-10-km,jelenia-gora,2014,3879,2619562/">Mojek Michał</a></td><td class='best'>00:45:45</td><td class='event'>

<a href="/pl/wyniki/2014/11/11/bieganie/bieg-niepodleglosci,3879/">Bieg Niepodległości</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2014-11-11</td></tr><tr class='row2 Zawody'><td>#26<td class='taken'>



<a href="#_blank" data-poload="/pl/results/2823/2163757/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>824</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
58
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/letni-bieg-piastow-jakuszycka-dziesiatka-biegi-gorskie-10-km,szklarska-poreba,2014,2823,2163757/">Mojek Michał</a></td><td class='best'>00:54:58</td><td class='event'>

<a href="/pl/wyniki/2014/08/30/biegi-gorskie/letni-bieg-piastow-jakuszycka-dziesiatka,2823/">Letni Bieg Piastów - Jakuszycka Dziesiątka</a>

</td><td class='distance'>10 km</td><td class='sport'>Biegi Górskie</td><td class='date'>2014-08-30</td></tr><tr class='row1 Zawody'><td>#27<td class='taken'>



<a href="#_blank" data-poload="/pl/results/358/453676/popover/athlete/mojek-michal/" data-toggle="button" class="btn btn-mini" data-original-title="<i class='icon-edit'></i> Zapisane"><i title="This item is claimed. Click to show." alt="Zapisane"></i>
    <img class="imgavatar" src=https://static.enduhub.com/default-user-avatar.png />
</a>

</td><td class='nr'>9564</td><td class='yob'>80</td><td class='place'>










<p class="centered-text">
3091
</p>
</td><td class='name'><a href="/pl/mojek-michal/koncowy-wynik/biegnij-warszawo-2011-bieganie-10-km,warszawa,2011,358,453676/">Mojek Michał</a></td><td class='best'>00:54:19</td><td class='event'>

<a href="/pl/wyniki/2011/10/02/bieganie/biegnij-warszawo-2011,358/">Biegnij Warszawo 2011</a>

</td><td class='distance'>10 km</td><td class='sport'>Bieganie</td><td class='date'>2011-10-02</td></tr>



</tbody>

      	      
    </table>
    






    
  </form>
</div>


<div class="alert">
  Nie znalazłeś wszystkiego ? Zgłoś wyniki tutaj: <a href="/pl/dodaj/nowe-wyniki/"><b>Zgłoś wyniki</b></a>. Otrzymasz potwierdzenie kiedy je załadujemy.</li>
</div>






	
 
	<!-- Modal -->
	
	
	

	<div class="footerbar">
	    <ul class="footerbar">
		
		<li><a href="/pl/endu/help/">Help</a><span class="divider">|</span></li>
		<li><a href="/pl/regulamin/">Regulamin</a><span class="divider">|</span></li>
		<li><a href="/pl/polityka-prywatnosci/">Polityka prywatności</a><span class="divider">|</span></li>
		<!--  <li><a href="/pl/bezpiecze%C5%84stwo/">Bezpieczeństwo</a><span class="divider">|</span></li> -->
		<li><a href="/pl/o-nas/">O nas</a><span class="divider">|</span></li>
		<li><a href="/pl/kontakt/">Kontakt</a><span class="divider">|</span></li>
		<li><a href="/pl/dodaj/nowe-wyniki/">Zgłoś wyniki</a><span class="divider">|</span></li>
		<li><a href="/pl/usu%C5%84/moje/dane/">Usuń moje dane</a><span class="divider">|</span></li>
		<li><a href="/pl/newsletter/">Newsletter</a><span class="divider">|</span></li>
		<li><a href="/newsletter/masz-pomysl-na-aplikacje-fitness-skorzystaj-z-enduhub-api/">API</a><span class="divider">|</span></li>
		<li><a href="/newsletter/buduj-z-nami-enduhub-prawdopodobnie-najwieksza-baze-wynikow-w-necie/"</a>Buduj z nami Enduhub <span class="divider">|</span></li>
		<li><a href="/pl/sponsored/results/"</a>Wyniki sponsorowane</li>
		
		<!-- Language field  -->
		
		
		
		
		<a href="/en/"><li class="pull-right flag flag-en"></li></a>
		
		
		
		<a href="/pl/"><li class="pull-right flag flag-pl"></li></a>
		
		
		
		<a href="/es/"><li class="pull-right flag flag-es"></li></a>
		
		
		<li class="pull-right"><a href="#">(c) 2019</a>&nbsp; &nbsp;</li>
	    </ul>

	    
	    

<div class="recommended"><h6>Polecane zawody :</h6></div>
<ul class="footerbar">
    
    <li title="Poznan półmaraton"><a href="/pl/strona-zawodow/poznan-polmaraton,2/">Poznan półmaraton</a><span class="divider">|</span></li>
    
    <li title="Poznań maraton"><a href="/pl/strona-zawodow/poznan-maraton,12/">Poznań maraton</a><span class="divider">|</span></li>
    
    <li title="Maraton Warszawski"><a href="/pl/strona-zawodow/maraton-warszawski,20/">Maraton Warszawski</a><span class="divider">|</span></li>
    
    <li title="Półmaraton Warszawski"><a href="/pl/strona-zawodow/polmaraton-warszawski,22/">Półmaraton Warszawski</a><span class="divider">|</span></li>
    
    <li title="Cracovia Maraton"><a href="/pl/strona-zawodow/cracovia-maraton,29/">Cracovia Maraton</a><span class="divider">|</span></li>
    
    <li title="Wrocław Maraton"><a href="/pl/strona-zawodow/wroclaw-maraton,41/">Wrocław Maraton</a><span class="divider">|</span></li>
    
    <li title="Maraton Dębno"><a href="/pl/strona-zawodow/maraton-debno,46/">Maraton Dębno</a><span class="divider">|</span></li>
    
</ul>


	    

	    <div class="recommended"><h6>Mobile :</h6></div>
	    <p>
		<a href='https://play.google.com/store/apps/details?id=com.enduhub.enduhubmobile&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'><img alt='Google Play' width="200px" src='https://play.google.com/intl/en_us/badges/images/generic/pl_badge_web_generic.png'/></a>
	    </p>

	    <div class="recommended"><h6>Partnerzy :</h6></div>

	    <p class="center-text">
		<a href="/" title="zawody & wyniki w jednym miejscu"><img alt="wyniki sporty wytrzymałośćiowe, bieganie, kolarstwo, MTB, triatlon, pływanie, duathlon, maraton, multisport" src="https://static.enduhub.com//endupac60.png"></a>
		<a href="https://www.poznanbiega.pl" title="Polecamy stronę o biegach w Wielkopolsce: PoznanBiega.pl"><img alt="poznanbiega.pl" src=https://static.enduhub.com/poznanbiegapl150.png></a>
		<!--
		<a href="http://tritour.com.pl/" title="Tritour - cykl imprez triathlonowych"><img alt="http://tritour.pl" src=https://static.enduhub.com/tritour.png style='padding:5px;width:200px;'></a>
		-->
		<a href="http://www.cityzenklub.pl" title="CityZen więcej niż klub sportowy"><img alt="http://www.cityzenklub.pl" src=https://static.enduhub.com/beefree_cityzen.png style='padding:5px;width:150px;'></a>
		<!--  <a href="https://www.facebook.com/CrossFitRankor" alt="CrossFit Rankor Poznan" title="CrossFit Rankor Poznan"><img alt="https://www.facebook.com/CrossFitRankor.pl" src=https://static.enduhub.com/rankor.png></a>      -->
		<a href="http://12tri.pl" alt="12tri" title="12tri"><img alt="http://12tri.pl" src=https://static.enduhub.com/12tri_horizontal.png></a>      
		<!--  <a href='http://3xjanusz.pl' target='_blank' title='3xJanusz - Profesjonalny amatorski blog o triathlonie'><img src='http://3xjanusz.pl/reklama_3.png' alt='3xJanusz - Profesjonalny amatorski blog o triathlonie' style='border:0;width:150px;' /></a> -->
		<a href='http://ligabiegowa.pl' target='_blank' title='liga biegowa'><img src='https://static.enduhub.com/LB_logo200px.png' alt='ligabiegowa.pl'  /></a>
		<a href="/" title="zawody & wyniki w jednym miejscu"><img alt="zawody & wyniki w jednym miejscu" src="https://static.enduhub.com//endupac60.png"></a>
	    </p>
	</div>
	

	
	<div id="analitycs">
	    <script type="text/javascript">
 var _gaq = _gaq || [];
 _gaq.push(['_setAccount', 'UA-36231251-1']);
 _gaq.push(['_trackPageview']);
 
 (function() {
     var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
     ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
     var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
 })();
</script>

	</div>
	

	<!-- cookie info -->
	
	
	<div class="alert alert-block alert-info fade in">
	    <button type="button" class="close" data-dismiss="alert">×</button>
	    <p>Ta strona używa Cookies. Dowiedz się więcej o celu ich używania - przeczytaj naszą politykę prywatności.Korzystając ze strony wyrażasz zgodę na używanie cookie, zgodnie z aktualnymi ustawieniami przeglądarki.</p>
	    <a class="btn btn-info inline-get" href="/pl/cookie/privacy/accept/">enduhub.com jest thebeściak więc się zgadzam !</a>
	    <a href="/pl/polityka-prywatnosci/">Polityka prywatności</a>
	</div>
	
	
	
	

	<!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
	<!-- [if lt IE 9]> <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script> <![endif]-->

	<!-- Localization for javascript needs to be included as well. Django supports JS localization but it I was unable to make it work -->
	<script>	    
	 var ready = 'Proszę czekać ......';
	 var error = 'Błąd podczas przetwarzania ! Proszę spróbuj ponownie.';
	</script>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js"></script>
	<script type="text/javascript" src="https://static.enduhub.com/enduhub.min.js?v=2"></script>
	
	
	<!-- Load jquery and stick datapicker to #datapicker id. -->
	<script>
	 $(document).ready(function() {
	     $(function() {
		 $.datepicker.setDefaults($.datepicker.regional['pl']);
	     });
	     $(function() {
		 $( "#datepicker" ).datepicker( $.datepicker.regional[ 'pl' ]);
	     });
	     $(function() {
		 $('#enduModal').modal();
	     });
	 });
	</script>
	<script>
	 $(document).ready(function() {
	    if (!localStorage.mission) {
	         $('.alert-welcome-box').show('fast');
	    }
	    $('.welcome-alert-button').click(function() {
	         localStorage.mission=1;
		 $.ajax
		 ({ 
		     url: "/pl/endu/mission/accept/",
		     method: 'POST',
		 });
	     });
	 });
	</script>

	<!-- Responsive full screen background script -->
	<script>
	 /* fix vertical when not overflow
	    call fullscreenFix() if .fullscreen content changes */
	 function fullscreenFix(){
	     var h = $('body').height();
	     // set .fullscreen height
	     $(".content-b").each(function(i){
		 if($(this).innerHeight() <= h){
		     $(this).closest(".fullscreen").addClass("not-overflow");
		 }
	     });
	 }
	 $(window).resize(fullscreenFix);
	 fullscreenFix();

	 /* resize background images */
	 function backgroundResize(){
	     var windowH = $(window).height();
	     $(".background").each(function(i){
		 var path = $(this);
		 // variables
		 var contW = path.width();
		 var contH = path.height();
		 var imgW = path.attr("data-img-width");
		 var imgH = path.attr("data-img-height");
		 var ratio = imgW / imgH;
		 // overflowing difference
		 var diff = parseFloat(path.attr("data-diff"));
		 diff = diff ? diff : 0;
		 // remaining height to have fullscreen image only on parallax
		 var remainingH = 0;
		 if(path.hasClass("parallax")){
		     var maxH = contH > windowH ? contH : windowH;
		     remainingH = windowH - contH;
		 }
		 // set img values depending on cont
		 imgH = contH + remainingH + diff;
		 imgW = imgH * ratio;
		 // fix when too large
		 if(contW > imgW){
		     imgW = contW;
		     imgH = imgW / ratio;
		 }
		 //
		 path.data("resized-imgW", imgW);
		 path.data("resized-imgH", imgH);
		 path.css("background-size", imgW + "px " + imgH + "px");
	     });
	 }
	 $(window).resize(backgroundResize);
	 $(window).focus(backgroundResize);
	 backgroundResize();
	</script>
	<!-- End of responsive full screen backgriund script -->

	<script type="application/ld+json">
	 {
	     "@context": "http://schema.org",
	     "@type": "WebSite",
	     "url": "https://www.enduhub.com/",
	     "potentialAction": {
		 "@type": "SearchAction",
		 "target": "https://enduhub.com/pl/search/?name={search_term_string}",
		 "query-input": "required name=search_term_string"
	     }
	 }
	</script>
	
    </body>
</html>
"""
