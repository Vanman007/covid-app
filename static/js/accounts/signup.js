
// fb lib
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '419079382794830',
      cookie     : true,
      xfbml      : true,
      version    : 'v9.0'
    });
      
    FB.AppEvents.logPageView();  

    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
      
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));


function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}


function statusChangeCallback(response) {
  if (response.status === 'connected') {
    // Logged into your webpage and Facebook.
    console.log("loggedin")
  } else {
    console.log("not logged in")
    // The person is not logged into your webpage or we are unable to tell. 
  }
}

