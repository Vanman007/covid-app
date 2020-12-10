
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


//google auth

//   gapi.auth2.authorize({
//     client_id: '770688674608-0n9tic1b0g45i0h9k6s7ohf64e12fqbb.apps.googleusercontent.com',
//     scope: 'email profile openid',
//     response_type: 'id_token permission'
//   }, function(response) {
//     if (response.error) {
//       // An error happened!
//       return;
//     }
//     // The user authorized the application for the scopes requested.
//     var accessToken = response.access_token;
//     var idToken = response.id_token;
//     // You can also now use gapi.client to perform authenticated requests.
//   });