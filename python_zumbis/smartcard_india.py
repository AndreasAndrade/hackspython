# coding: utf-8
__author__ = 'Andreas'

# coding: utf-8
import urllib2
import os


source = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" >
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-gb" lang="en-gb" dir="ltr" >
<head>

<script type="text/javascript" src="https://uidai.gov.in//plugins/system/js_loadjquery/libraries/jquery/jquery-1.7.1.min.js"></script><script type="text/javascript">jQuery.noConflict();</script>
  <base href="https://uidai.gov.in/library/references.html" />
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="author" content="Super User" />
  <meta name="generator" content="Joomla! - Open Source Content Management" />
  <title>UIDAI - References</title>
  <link href="https://uidai.gov.in/hi/library-hi/references.html" rel="alternate" hreflang="hi-IN" />
  <link href="https://uidai.gov.in/ta/library-ta/references.html" rel="alternate" hreflang="ta-IN" />
  <link href="https://uidai.gov.in/kn/library-kn/references.html" rel="alternate" hreflang="kn-IN" />
  <link href="https://uidai.gov.in/mr/library-mr/references.html" rel="alternate" hreflang="mr-IN" />
  <link href="https://uidai.gov.in/bn/library-bn/references.html" rel="alternate" hreflang="bn-IN" />
  <link href="https://uidai.gov.in/gu/library-gu/references.html" rel="alternate" hreflang="gu-IN" />
  <link href="https://uidai.gov.in/pu/library/references.html" rel="alternate" hreflang="pu-IN" />
  <link href="https://uidai.gov.in/ml/library/references.html" rel="alternate" hreflang="ml-IN" />
  <link href="/templates/beez5/favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
  <link rel="stylesheet" href="/modules/mod_sp_news_highlighter/assets/css/style.css" type="text/css" />
  <link rel="stylesheet" href="/modules/mod_jpanel/assets/css/style.css" type="text/css" />
  <link rel="stylesheet" href="/modules/mod_ojaccordionmenu/assets/css/oj-accordmenu.css" type="text/css" />
  <link rel="stylesheet" href="/modules/mod_ojaccordionmenu/assets/css/orange.css" type="text/css" />
  <link rel="stylesheet" href="/media/mod_languages/css/template.css" type="text/css" />
  <style type="text/css">
.mooquee-text{position:absolute;}
.mod_simple_marquee_content{overflow:hidden;white-space:nowrap;position:relative;}
#sp-nh151 {width:100%;color:#000;height:25px;}.sp-nh-item{background:#F9F9F9}.sp-nh-buttons {width:155px}a.sp-nh-link {color:#133180}a.sp-nh-link:hover {color:#006699}.sp-nh-buttons,.sp-nh-item,.sp-nh-prev,.sp-nh-next {height:25px;line-height:25px}.sp-nh-prev,.sp-nh-next{background-image: url(/modules/mod_sp_news_highlighter/assets/images/style1.png)}
#sidejPanel_131_right .jpanelContent{height: 232px; }#sidejPanel_131_right .jpanelContent{width: 170px; }#sidejPanel_131_right .jpanelHandle{background:url(/images/menu_button_en-GB.png);width:16px;height:220px;} #sidejPanel_131_right .jpanelContent{ border:0px solid #F5801F; }#sidejPanel_131_right .jpanelContent{background-color: #494949; }#sidejPanel_131_right{right:-181px; top:53%;}
#sidejPanel_131_right .jpanelHandle p{margin: 0;}
#sidejPanel_131_right .jpanelHandle{border-radius:5px 0 0 5px;}
#sidejPanel_131_right .jpanelHandle, #sidejPanel_131_right .jpanelContent{float:right;}

  </style>
  <script src="/media/system/js/mootools-core.js" type="text/javascript"></script>
  <script src="/media/system/js/core.js" type="text/javascript"></script>
  <script src="/media/system/js/caption.js" type="text/javascript"></script>
  <script src="/media/system/js/mootools-more.js" type="text/javascript"></script>
  <script src="/media/system/js/jquery.js" type="text/javascript"></script>
  <script src="/media/system/js/jquery-ui.js" type="text/javascript"></script>
  <script src="/templates/beez5/javascript/md_stylechanger.js" type="text/javascript" defer="defer"></script>
  <script src="/templates/beez5/javascript/script.js" type="text/javascript" defer="defer"></script>
  <script src="/modules/mod_mh_simple_marquee/tmpl/mooquee.js" type="text/javascript"></script>
  <script src="/modules/mod_sp_news_highlighter/assets/js/sp_highlighter.js" type="text/javascript"></script>
  <script src="/modules/mod_jpanel/assets/js/jpanel.min.js" type="text/javascript"></script>
  <script type="text/javascript">
window.addEvent('load', function() {
				new JCaption('img.caption');
			});
window.addEvent("domready", function() {
   var options = {};
   $$(".mod_simple_marquee").each(function(item) {
       options["marWidth"] = item.getParent("div").getSize().x;
       options["marHeight"] = item.getParent("div").getSize().y;
       var config = item.getChildren()[0].getProperty("rel").split("|");
       config.each(function(cfg) {
           var tmp = cfg.split("=");
           options[tmp[0]] = tmp[1];
       });
       new mooquee(item.getChildren()[1], options);
   });
});
$jp.fn.textWidth = function(){
  var html_org = $jp(this).html();
  var html_calc = "<span>" + html_org + "</span>";
  $jp(this).html(html_calc);
  var width = $jp(this).find("span:first").width();
  $jp(this).html(html_org);
  return width;
};

	$jp(document).ready(function() {

		hoverJpanel("#sidejPanel_131_right");
	});

  </script>
  <script type="text/javascript">jQuery.noConflict();</script>
  <style type="text/css">
		.jt-tooltip{
   			display: inline;
    		position: relative;
		}
		.jt-tooltip:hover:after{
    		background: #333;
    		background: rgba(0,0,0,.8);
    		border-radius: 5px;
    		bottom: 26px;
    		color: #fff;
    		content: attr(title);
    		left: 20%;
    		padding: 5px 15px;
    		position: absolute;
    		z-index: 98;
    		width: 220px;
		}
		.jt-tooltip:hover:before{
    		border: solid;
    		border-color: #333 transparent;
    		border-width: 6px 6px 0 6px;
    		bottom: 20px;
    		content: "";
    		left: 50%;
    		position: absolute;
    		z-index: 99;
		}
		</style>

<link rel="stylesheet" href="/templates/beez5/css/style_en-GB.css" type="text/css" />
<link rel="stylesheet" href="/templates/beez5/css/layout_en-GB.css" type="text/css" media="screen"/>
<link rel="stylesheet" href="/templates/beez5/css/gallery.css" type="text/css" media="screen"/>
<link rel="stylesheet" href="/templates/beez5/css/jquery-ui.css" type="text/css" />
<link rel="stylesheet" href="/templates/beez5/css/jquery.autocomplete.css" type="text/css" />
<link rel="stylesheet" href="/templates/system/css/system.css" type="text/css" />
    <link rel="stylesheet" href="/templates/beez5/css/general.css" type="text/css" />
<script type="text/javascript" src="/templates/beez5/javascript/hide.js"></script>
<script type="text/javascript">
//<![CDATA[
  var big ='72%';
  var small='53%';
  var altopen='is open';
  var altclose='is closed';
  var bildauf='/templates/beez5/images/plus.png';
  var bildzu='/templates/beez5/images/minus.png';
  var rightopen='Open info';
  var rightclose='Close info';
  var fontSizeTitle='Font size';

var bigger="<img src='/templates/beez5/images/textsizePlus.gif' alt='Bigger' />";
var reset="<img src='/templates/beez5/images/textsizeNormal.gif' alt='Reset' />";
var smaller="<img src='/templates/beez5/images/textsizeMinus.gif' alt='Smaller' />";

  var biggerTitle='Increase size';
  var resetTitle='Revert styles to default';
  var smallerTitle='Decrease size';
//]]>
</script>
<script type="text/javascript" src="/templates/beez5/javascript/uid.js"></script>
<style type="text/css">a#vlb{display:none}</style>
  <script type="text/javascript">
//jQuery(document).ready(function() {
//                jQuery("#feedback").click(function(){
//                     jQuery(".fbbc").slideToggle(1000);
//                });

//});
</script>
</head>
<body>
<div id="all">
<div id="wrapper">
  <div id="header">
<div id="topbar" style="display:block;">
  <div id="uidheader_lft">
    <div id="anktopbar_lft" style="font-size: 11px; margin-top: 4px; margin-left: 0px;">
        <div id="anktopbars1"><a style="color:#ffffff;" href="#maincontent">Go to main content  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></div>
        <div id="anktopbars2"><a style="color:#ffffff;" href="#tpnav">Go to navigation</a></div>
      </div>

     <div style="float: right; margin-right: 113px;position:relative;">
        <div class="fdbck-div">
          <div class="fbdk-txt-div">
            <!--<div id="feedback" onmouseover="fdShow();" onmouseout="fdHide();">Feedback</div>-->
             <div id="feedback"> <a style="color:#ffffff; font-weight:bold; text-decoration:none;" href="http://resident.uidai.net.in" target="_blank">Grievance</a></div>
            <div style="clear:both;"></div>
          </div>
          <!--<div class="fbbc">
            <p class="fb-p">Please Share Your Feedback on Multilingual Website at...<a href="mailto:kmportal@uidai.gov.in">kmportal@uidai.gov.in</a></p>
          </div>-->
       </div>

        <div class="lang-txt">Language:</div>
        <div id="uidlang">
          <div class="moduletable">
 <div class="mod-languages">

	<form name="lang" method="post" action="https://uidai.gov.in/library/references.html">
	<select class="inputbox" onchange="document.location.replace(this.value);" >
		<option dir="ltr" value="/as/" >
		Assamese</option>


		<option dir="ltr" value="/hi/library-hi/references.html" >
		Hindi</option>


		<option dir="ltr" value="/ta/library-ta/references.html" >
		Tamil</option>


		<option dir="ltr" value="/kn/library-kn/references.html" >
		Kannada</option>


		<option dir="ltr" value="/mr/library-mr/references.html" >
		Marathi</option>


		<option dir="ltr" value="/bn/library-bn/references.html" >
		Bengali</option>


		<option dir="ltr" value="/gu/library-gu/references.html" >
		Gujarati</option>


		<option dir="ltr" value="/pu/library/references.html" >
		Punjabi</option>


		<option dir="ltr" value="/od/" >
		Odia</option>


		<option dir="ltr" value="/ml/library/references.html" >
		Malayalam</option>


		<option dir="ltr" value="/te/" >
		Telugu</option>


				<option style="display:none" dir="ltr" value="/ur/" >
		Urdu</option>

		<option dir="ltr" value="/library/references.html" selected="selected">
		English</option>


		</select>
	</form>

</div></div>

        </div>
        <div style="clear:both;"></div>
      </div>
      <div style="clear:both;"></div>

   </div></div>

    <div class="wrap">
      <div id="logo" style="display:none;">
      <a href="/index.php"><img src="/templates/beez5/images/logo.png" id="logo1" alt="Logo" /></a></div>
      <a href="/index.php"><img src="/images/authority_en-GB.png" id="logo2" alt="Authority Logo" /></a>
      <div id="rightlogo">
      <a href="/index.php"><img src="/images/logo_en-GB.gif" height="65px" alt="Logo" /></a>
</div>
    </div>
  </div>
  <div id="uidbanner" class="uidbannercls">
  <div class="moduletable">
 <div id="headerimg">
  	<img src="/images/banners/resource-center.png" height="225" id="bannerimage" alt="Banner" />
  	<p class="slogan" id="slogan" align="center">Resource Center</p>
</div>

</div>

  </div>

  <div id="mainnav">
       <div class="wrap">
            <div id="searchbox">
                <div class="moduletable">
 <script type="text/javascript">
function trim(s)
{
	return s.replace(/^\s+|\s+$/g,"");
}

function chkSearchFrm()
{
	var searchVal=document.getElementById('q').value;
	if(trim(searchVal)=='Search' || trim(searchVal)==''){
	alert('Please enter your search keyword.');
	return false;
	}
return true;
}
</script>

<form action="/library/references.html" method="post" name="searchform" id="searchform" onsubmit="return chkSearchFrm();" autocomplete="off">
<input type="text" name="searchword" id="q" value="Search" onfocus="if (this.value=='Search') {this.value='';}"  onblur="if (this.value=='') {this.value='Search';}"/>
<input name="submit" id="search" type="submit" value="&nbsp;"  />
<input type="hidden" name="task" value="search" />
<input type="hidden" name="option" value="com_search" />
<input type="hidden" name="Itemid" value="" />
</form></div>

         </div>
    <div class="topmainmenu">
              <div class="moduletable_topmenu">

<ul class="menu">
<li class="item-1200"><a href="/" >Home</a></li><li class="item-1202"><a href="/quick-links-en/resident-en.html" >Resident</a></li><li class="item-1203"><a href="/quick-links-en/registrar-en.html" >Registrar</a></li><li class="item-1204"><a href="/quick-links-en/partner-en.html" >Partner</a></li><li class="item-1205"><a href="/quick-links-en/student-en.html" >Students</a></li><li class="item-1206"><a href="/quick-links-en/others-en.html" >Others</a></li></ul>
</div>
<a name="tpnav"></a>
         </div>

       </div>
  </div>
  <div class="wrap">
    <div id="navinner">
    <div id="sidemenu">
      <div class="moduletable_sidemenu">

<div class="_sidemenu"  >
	<div id="sidejPanel_131_right" class="jPanel">
					<div class="jpanelContent" style="background: url('/images/rightnavbg.png') bottom repeat-x #494949;">

	<div><div>		<div class="moduletable">

<ul class="menu">
<li class="item-105"><a href="/aapka-aadhaar.html" >Aapka Aadhaar</a></li><li class="item-106"><a href="/about-uidai.html" >About UIDAI</a></li><li class="item-1274"><a href="/fi-e-kyc.html" >FI &amp; e-KYC</a></li><li class="item-2206"><a href="/state-wise-aadhaar.html" >State-wise Aadhaar Ranking</a></li><li class="item-110"><a href="/resource-center.html" >Resource Center</a></li><li class="item-117"><a href="/news-media-center.html" >News &amp; Media Center</a></li><li class="item-1276"><a href="/updates.html" >Updates</a></li><li class="item-113"><a href="/rti-en.html" >RTI</a></li><li class="item-1256 active"><a href="/library/references.html" >Reference Docs</a></li><li class="item-1275"><a href="/vacancies-uidai.html" >Current Vacancies</a></li><li class="item-1245"><a href="/workshop-presentation.html" >Workshops</a></li></ul>
		</div>
	</div></div>		</div>

		<div class="jpanelHandle"><p>&nbsp;</p><p>&nbsp;</p></div>
		</div>
</div></div>
<div class="moduletable_orange">
 <h3><span
	class="backh"><span class="backh2"><span class="backh3">Resource Center</span></span></span></h3>
 <script type="text/javascript">
jQuery(document).ready(function() {
			//slides the element with class "menu_body" when mouse is over the paragraph
		jQuery('#accordion_ifjhh p.menu_head').mouseover(function() {
			jQuery(this).next("div.menu_body").slideDown(500).siblings("div.menu_body").slideUp("slow");
		});
	});
</script>
<div id="ojaccord-menu">
            <!-- BEGIN Standalone Accordion Menu -->
        <div id="accordion_ifjhh" class="menu_list">
                <p class="menu_head"><a id="MenuItem129"  href="/aadhaar-technology.html">Aadhaar Technology</a></p>
                <p class="menu_head haschild"><a id="MenuItem130"  href="/biometric-devices.html">Biometric Devices</a></p>
                    <div class="menu_body">
               <ul>
                                <li class="oj-accord_li">
                        <a id="MenuItem2200"  class="" href="/biometric-devices/biometric-device-certification.html">Biometric Device Certification</a>

                                </li>
                        </ul>
        </div>
                <p class="menu_head"><a id="MenuItem131" target="_blank" href="http://www.stqc.gov.in/content/bio-metric-devices-testing-and-certification">Certified Biometric Devices</a></p>
                <p class="menu_head haschild active"><a id="MenuItem132"  href="/library.html">Library</a></p>
                    <div class="menu_body"style="display:block;">
               <ul>
                                <li class="oj-accord_li">
                        <a id="MenuItem133"  class="" href="/library/uid-documents.html">UID Documents</a>

                                </li>
                                <li class="oj-accord_li">
                        <a id="MenuItem176"  class="" href="/library/archives.html">Archives</a>

                                </li>
                                <li class="oj-accord_li">
                        <a id="MenuItem177"  class="sub_active" href="/library/references.html">References</a>

                                </li>
                                <li class="oj-accord_li">
                        <a id="MenuItem1259"  class="" href="/library/sanction-orders.html">Sanction Orders</a>

                                </li>
                        </ul>
        </div>
                <p class="menu_head"><a id="MenuItem178"  href="/public-announcements.html">Public Announcements</a></p>
                <p class="menu_head haschild"><a id="MenuItem184"  href="/financial-inclusion.html">Financial Inclusion & e-KYC</a></p>
                    <div class="menu_body">
               <ul>
                                <li class="oj-accord_li">
                        <a id="MenuItem2196"  class="" href="/financial-inclusion/archives.html">Archives</a>

                                </li>
                        </ul>
        </div>
                <p class="menu_head haschild"><a id="MenuItem181"  href="/rti.html">RTI</a></p>
                    <div class="menu_body">
               <ul>
                                <li class="oj-accord_li">
                        <a id="MenuItem282"  class="" href="/rti/rti-requests.html">RTI Requests</a>

                                </li>
                        </ul>
        </div>
                <p class="menu_head"><a id="MenuItem182"  href="/parliament-questions.html">Parliament Questions</a></p>
                <p class="menu_head"><a id="MenuItem183"  href="/finance-budgets.html">Finance & Budgets</a></p>
        </div>
    <!-- BEGIN Standalone Accordion Menu -->
</div></div>

        <div id="fontsize" align="right"></div>
    </div>
<div class="nav2top">&nbsp;</div>
<div id="nav2"><div class="moduletable">


<div class="custom"  >
	<div style="padding: 5px;">
<h4 style="margin: 0px 0px 6px 1px; color: white;">Aadhaar Services</h4>
<a href="https://resident.uidai.net.in/" target="_blank" style="font-size: 11px; margin: 0px 0px 3px 0px; color: #eef1f2; text-decoration: underline;"> Enrolment/Download E-aadhaar/Update</a> <strong> <a href="https://resident.uidai.net.in/update-data" target="_blank" style="font-size: 13px; color: #eef1f2; text-decoration: underline;"> Update your Aadhaar Data</a> </strong></div></div>
</div>
</div>
<div class="nav2bottom">&nbsp;</div>

<div id="nav22"></div>

      <div class="module">
        <div class="moduletable_menucontact">

<ul class="menu">
<li class="item-274"><a href="/uidai-contacts.html" >UIDAI Contacts</a></li><li class="item-293"><a href="/regional-offices.html" >Regional Offices</a></li></ul>
</div>

      </div>
      <div class="module">
        <div class="moduletable">


<div class="custom"  >
	<p style="height: 1px;"> </p>
<p><strong>Unique Identification Authority of India</strong><br /> Government of India<br /> 3rd Floor, Tower II<br /> Jeevan Bharati Building<br /> Connaught Circus<br /> New Delhi - 110001<br /><br /> <strong>TOLL FREE</strong> 1800-300-1947</p>
<hr /></div>
</div>

      </div>
      <div class="module">
        <div class="moduletable">


<div class="custom"  >
	<div id="bookmarks" class="module"><!--<a href="#"><img src="/images/fbicon.png" border="0" alt="Facebook" /></a>
<a href="#"><img src="/images/twicon.png" border="0" alt="Twitter" /></a>--> <a href="http://www.youtube.com/user/aadhaaruid" target="_blank"> <img src="/images/youtube.png" border="0" alt="youtube" /></a></div></div>
</div>

      </div>
    </div>
    <div id="container">
        <div id="breadcrumbs">

        </div>

<div id="system-message-container">
</div>
        <a name="maincontent"></a><div class="item-page">

	<h2>
			References		</h2>








<div id="childheadline">Aadhaar Technical Documents</div>
<ul>
<li><a href="/images/aadhaar_registered_devices_1_0.pdf" target="_blank">Aadhaar Registered Devices Specification 1.0</a></li>
<li><a href="/UID_PDF/Working_Papers/Aadhaar_ABIS_API.pdf" target="_blank">ABIS API 1.0</a></li>
<li><a href="/images/iris_poc_report_14092012.pdf" target="_blank">IRIS Authentication Accuracy – PoC Report </a></li>
<li><a href="/images/role_of_biometric_technology_in_aadhaar_authentication_020412.pdf" target="_blank">Role of Biometric Technology in Aadhaar Authentication - Detailed Report</a></li>
<li><a href="/UID_PDF/Working_Papers/UID_Biometrics_Capture_API_draft.pdf" target="_blank">Biometric Capture Device API</a></li>
<li><a href="/UID_PDF/Working_Papers/UID_Biometrics_Capture_API_draft.pdf" target="_blank">UID Biometrics Capture API</a></li>
<li><a href="/UID_PDF/Working_Papers/UID_and_iris_paper_final.pdf" target="_blank">Inclusion of Iris in the UID</a></li>
<li><a href="http://www.iba.org.in/upload/MicroATM_Standards_v1.5.1_Clean.pdf" target="_blank">Micro ATM standards Version 1.4</a></li>
<li><a href="/images/uid_numbering_scheme_1.pdf" target="_blank">UID numbering scheme</a></li>
<li><a href="/images/aadhaar_kyc_api_1_0_final.pdf" target="_blank">e-KYC API Document Version 1.0 </a></li>
<li><a href="/images/FrontPageUpdates/aadhaar_otp_request_api_1_5.pdf" target="_blank">Aadhaar One Time Pin (OTP) API 1.5</a></li>
<li><a href="/images/FrontPageUpdates/aadhaar_bfd_api_1_6.pdf" target="_blank">Aadhaar Best Finger Detection (BFD) API 1.6</a></li>
<li><a href="/images/FrontPageUpdates/aadhaar_authentication_api_1_6.pdf" target="_blank">Aadhaar Authentication API 1.6</a></li>
<li><a href="/images/aadhaar_biometric_sdk_api_2_0.pdf" target="_blank">Aadhaar Biometric SDK API 2.0</a></li>
<li><a href="/images/detailed_poc_10_report_ver12a_23052013.pdf" target="_blank">IRIS Kind-7 Authentication Accuracy- PoC Report</a></li>
<li><a href="/images/AadhaarTechnologyStrategy_March2014.pdf" target="_blank">Aadhaar Technology Strategy, Ecosystem, Technology and Governance</a></li>
<li><a href="/images/AadhaarTechnologyArchitecture_March2014.pdf" target="_blank">Aadhaar Technology &amp; Architecture: Principles, Design, Best Practices and Key Learnings</a></li>
<li><a href="/images/AadhaarProductDoc_march2014.pdf" target="_blank">Aadhaar Product Document</a></li>
<li><a href="/images/resource/aadhaar_mobile_update_api_1_0.pdf" target="_blank">Aadhaar Mobile Update API 1.0</a></li>
<li><a href="/images/resource/aadhaar_otp_request_api_1_6.pdf" target="_blank">Aadhaar OTP Request API 1.6</a></li>
</ul>
<div id="childheadline">Task Force Reports/Working Papers</div>
<ul>
<li><a href="/UID_PDF/Working_Papers/aadhaar_auth_field_test_report_ver_1.0.pdf" target="_blank">Report on Joint Field Test of Aadhaar Authentication with CRIS on moving Trains</a></li>
<li><a href="/UID_PDF/Working_Papers/Circulated_Aadhaar_PDS_Note.pdf" target="_blank">UID and PDS</a></li>
<li><a href="/UID_PDF/Working_Papers/UIDandEducation.pdf" target="_blank">UID and Education</a></li>
<li><a href="/UID_PDF/Working_Papers/UIDandPublicHealth.pdf" target="_blank">UID and Public Health</a></li>
<li><a href="/UID_PDF/Working_Papers/UIDandNREGA.pdf" target="_blank">UID and NREGA</a></li>
<li><a href="/images/FrontPageUpdates/discussionpaperonaadhaarbasedfinancialinclusion15oct.pdf" target="_blank">Discussion paper on Aadhaar based Financial Inclusion</a></li>
<li><a href="/images/authDoc/whitepaper_aadhaarenabledservice_delivery.pdf" target="_blank">Aadhaar Enabled Service Delivery</a></li>
<li><a href="http://finmin.nic.in/reports/Interim_report_Task_Force_DTS.pdf" target="_blank">Interim Report of Task Force on Direct Transfer of Subsidies</a></li>
<li><a href="http://finmin.nic.in/reports/IT_Strategy_PDS.pdf" target="_blank">IT Strategy for PDS Task Force Report</a></li>
<li><a href="http://finmin.nic.in/reports/Report_Task_Force_Aadhaar_PaymentInfra.pdf" target="_blank">Aadhaar Enabled Unified Payment Infrastructure Task Force Report</a></li>
</ul>
<div id="childheadline">UIDAI Documents</div>
<ul>
<ul>
<li><a href="/images/news/om_and_motifications_of_aadhaar_link_birth_registration_27052015.pdf" target="_blank">Office Memorandum and Modifications of Aadhaar link Birth registration</a></li>
<li><a href="/images/resource/process_for_aadhaar_letters_returned_by_india_post_ver_1.3.2.pdf" target="_blank">Process for Aadhaar Letters Returned by India Post v 1.3.2</a></li>
<li><a href="/images/mou/uidai_data_update_policy_ver_2.3.1.pdf" target="_blank">UIDAI Data Update Policy Ver 2.3.1</a></li>
<li><a href="/images/mou/resident_enrolment_process_ver_2.2.1.pdf" target="_blank">Resident Enrolment Process Ver 2.2.1</a></li>
<li><a href="/UID_PDF/Front_Page_Articles/Documents/Strategy_Overveiw-001.pdf" target="_blank">UIDAI Strategy Overview</a></li>
<li><a href="/UID_PDF/Front_Page_Articles/Strategy/Exclusion_to_Inclusion_with_Micropayments.pdf" target="_blank">Micropayments</a></li>
<li><a href="/UID_PDF/Committees/Biometrics_Standards_Committee_report.pdf" target="_blank">Biometric Committee</a></li>
<li><a href="/UID_PDF/Committees/UID_DDSVP_Committee_Report_v1.0.pdf" target="_blank">Demographic Data Std.</a></li>
<li><a href="/UID_PDF/Front_Page_Articles/Events/AADHAAR_PDF.pdf" target="_blank">Communicating to a Billion</a></li>
<li><a href="/images/aadhaar_handbook_registrars_v3_04062013.pdf" target="_blank">Aadhaar Handbook for Registrars</a></li>
<li><a href="/images/FrontPageUpdates/uid_enrolment_poc_report.pdf" target="_blank">UID enrolment Proof of Concept Report</a></li>
<li><a href="/images/FrontPageUpdates/uid_doc_30012012.pdf" target="_blank">Analytics : Empowering operations - The UIDAI Experience</a></li>
<li><a href="/images/FrontPageUpdates/role_of_biometric_technology_in_aadhaar_jan21_2012.pdf" target="_blank">Role of Biometric Technology in Aadhaar</a></li>
<li><a href="/images/leveraging_aadhaar_telecom_sector_ver10_090412.pdf" target="_blank">Leveraging Aadhaar in the Telecom Sector Ver.-1.0</a></li>
<li><a href="/images/concept_paper_social_inclusion.pdf" target="_blank">Concept Paper-Social Inclusion</a></li>
<li><a href="/images/ekyc_policy_note_18122012.pdf" target="_blank">e-KYC Policy</a></li>
<li><a href="/images/tenders/procurement_manual_2014_with_appendices_01042014.pdf" target="_blank">Procurement Manual - 2014</a></li>
<li><a href="/images/mou/enrolment_and_update_archive.zip" target="_blank">Enrolment &amp; Update Archive</a></li>
<li><a href="/images/agreements_with_nisg_01122014.zip" target="_blank">Agreements with NISG</a></li>
</ul>
</ul>

</div>

    </div>
    <div class="clear"></div>
  </div>
<div><div class="moduletable">
 <script type="text/javascript">
	window.addEvent('domready',function(){
		var highlighter_sp1_id151 = new sp_highlighter($('sp-nh-items151'), {
			size: {width: -55, height: 25},
			fxOptions: {duration:  1000, transition: Fx.Transitions.Sine.easeOut},
			transition: 'cover-inplace-fade'		});

					highlighter_sp1_id151.addPlayerControls('previous', [$('sp-nh-prev151')]);
			highlighter_sp1_id151.addPlayerControls('next', [$('sp-nh-next151')]);


					highlighter_sp1_id151.play(5000);

	});
</script>
<div id="sp-nh151" class="sp_news_higlighter side-mod">
	<div class="sp-nh-buttons" style="width:155px">
		<span class="sp-nh-text">LATEST NEWS:</span>
					<div id="sp-nh-prev151" class="sp-nh-prev"></div>
			<div id="sp-nh-next151" class="sp-nh-next"></div>
			</div>
	<div id="sp-nh-items151" class="sp-nh-item">
			<div class="sp-nh-item">
			<a class="sp-nh-link" href="/../images/news/state_ut_wise_aadhaar_enrolment_ranking_as_on_31082015.pdf" target="_blank" style="text-decoration:none;font-size:0.800em;font-weight:bold;"><span class="sp-nh-title">State/UT wise ranking based on Aadhaar saturation as on 31st August, 2015</span></a>
			</div>
					<div class="sp-nh-item">
			<a class="sp-nh-link" href="/../images/news/schedule_for_aadhaar_workshop_18082015.pdf" target="_blank" style="text-decoration:none;font-size:0.800em;font-weight:bold;"><span class="sp-nh-title">Sensitisation Workshop on Aadhaar Seeding and Authentication Services</span></a>
			</div>
					<div class="sp-nh-item">
			<a class="sp-nh-link" href="/../images/news/aadhaar_mobile_app_launched_2015.pdf" target="_blank" style="text-decoration:none;font-size:0.800em;font-weight:bold;"><span class="sp-nh-title">UIDAI launches Aadhaar Mobile Android app</span></a>
			</div>
					<div class="sp-nh-item">
			<a class="sp-nh-link" href="/../images/news/stqc_certificate_of_registration_0001_25052015.pdf" target="_blank" style="text-decoration:none;font-size:0.800em;font-weight:bold;"><span class="sp-nh-title">UIDAI becomes ISO / IEC 27001:2013 Certified</span></a>
			</div>
					<div class="sp-nh-item">
			<a class="sp-nh-link" href="/../images/news/stqc_ceritifcate0001_25052015.pdf" target="_blank" style="text-decoration:none;font-size:0.800em;font-weight:bold;"><span class="sp-nh-title">Scope of ISMS Certification</span></a>
			</div>
					<div class="sp-nh-item">
			<a class="sp-nh-link" href="/../images/news/uidai_eoi_iris_30042015.pdf" target="_blank" style="text-decoration:none;font-size:0.800em;font-weight:bold;"><span class="sp-nh-title">Seeking Expression of Interest from Technology Solution Providers and device Manufacturers for POC of IRIS Device Specification Revision</span></a>
			</div>
			</div>
	<div style="clear:both"></div>
</div></div>
</div>
  <div id="footer">
    <div class="wrap">
      <div class="moduletable_footer">

<ul class="menu_footermenu">
<li class="item-101"><a href="/" >Home</a></li><li class="item-103"><a href="/uid-tenders.html" >Tenders</a></li><li class="item-111"><a href="/auth.html" >Authentication</a></li><li class="item-112"><a href="/terms-of-use.html" >Terms of Use</a></li><li class="item-173"><a href="/external-links.html" >External Links</a></li><li class="item-174"><a href="/privacy-policy.html" >Privacy Policy</a></li><li class="item-201"><a href="/disclaimer.html" >Disclaimer</a></li><li class="item-260"><a href="/sitemap.html" >Site Map</a></li><li class="item-114"><a href="/faq.html" >F.A.Q.</a></li><li class="item-116"><a href="/contactus.html" >Contact Us</a></li></ul>
</div>

    </div>
  </div>
  <div id="copyright">
<div class="moduletable">


<div class="custom"  >
	<p><span class="fRight">This website is best viewed in 1024x768 screen resolution.</span>Copyright © 2012 UIDAI All Rights Reserved.</p></div>
</div>

    <div class="mod_simple_marquee">
<a name="marqueeconfig" rel="speed=40|direction=left|pauseOnOver=1"></a>
<div class="mod_simple_marquee_content"><p id="note-txt" style="background:none repeat scroll 0 0 #f8f8f8;color:#133180;font-size:14px;text-align:left;width:100%;"><b>Choose Aadhaar! It is voluntary. “It is not mandatory for a citizen to obtain an Aadhaar Card.”</b></p>
 +++ <p id="note-txt" style="background:none repeat scroll 0 0 #f8f8f8;color:#000000;font-size:9px;text-align:left;width:100%;">NOTE: www.uidai.gov.in is the ONLY official website of the Unique Identification Authority of India (UIDAI) and no other websites using the term UIDAI/Aadhaar/UID or related terms should be considered as the official website of the Authority </p></div>
</div>
</div>
</div>
</div>
</body>
</html>
'''


# tag = '/uploads/coberturas/Ressaca-de-Carnaval-2015/'
tag = '<a href="'

site = 'https://uidai.gov.in/'

indice_atual = source.find(tag)

while indice_atual != -1:

    inicio_do_link = indice_atual + len(tag)  # len(tag) = 9
    fim_do_link = source.find('"', inicio_do_link)
    nome_do_arquivo = source[inicio_do_link:fim_do_link]
    if nome_do_arquivo.find('.pdf') != -1:
        print (source[indice_atual + len(tag):fim_do_link])
        pdf = nome_do_arquivo.split('/')[-1]
        print pdf

        url = site + nome_do_arquivo
        print (url)
        # audio = requests.get(url)
        try:
            arquivo = urllib2.urlopen(url).read()
        except:
            pass
        caminho = 'C:/Users/Andreas/Desktop/arquivos hackeados/smartcard_india'
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        # filef = open("C:/Users/Andreas/Desktop/afterfest/%s" % nome_do_audio, 'wb')
        filef = open(caminho + "/" + pdf, 'wb')
        #filef = open(nome_do_audio, 'wb')
        filef.write(arquivo)
        filef.close()

    indice_atual = source.find(tag, indice_atual + 1)

print 'terminou...........'
