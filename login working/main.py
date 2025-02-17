from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/", response_class=HTMLResponse)
# async def read_items():
#     html_content = """
#     <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel="stylesheet" href="login.css">
    
#     <title>Sign in page</title>
#     <style>
#     *{
#     margin: 0;
#     padding: 0;
#     font-family: sans-serif;
    

# }
# .hero{
#     height: 100%;
#     width: 100%;
#     background-image:linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4));
    
#     background-position: center;
#     background-size: cover;
#     position: absolute;
# }
# .form-box{
#     width: 380px;
#     height: 480px;
#     position: relative;
#     margin: 6% auto;
#     background: #fff;
#     padding: 5px;
#     overflow: hidden;
#     border-radius: 30px;
    
# }
# .button-box{

#     width: 220px;
#     margin: 35px auto; 
#     position: relative;
#     box-shadow: 0 0 20px 9px #ff61241f;    
#     border-radius: 30px;
# }
    
# .toggle-btn{ 
#     padding: 10px 30px;    
#     cursor: pointer;
#     background: transparent;
#     border: 0;
#     outline: none;
#     position: relative;
# }
# #btn{
#     top: 0;
#     left: 0;
#     position: absolute;
#     width:110px;
#     height: 100%;
#     background:linear-gradient(to right,#ff105f,#ffad06);
#     border-radius: 30px;
#     transition: .2s ;
# }
# .social-icons{
#     margin: 30px auto;
#     text-align: center;
# }
# .social-icons img{
#     width: 30px;
#     margin: 0 12px;
#     box-shadow: 0 0 20px 0 #7f7f7f3d ;
#     cursor: pointer;
#     border-radius: 50%;
# }
# .input-group{
#     top: 180px;
#     position: absolute; 
#     width: 280px;
#     transition: .5s;
# }
# .input-field{
#     width:100%;
#     padding: 10px 0;
#     margin: 5px 0;
#     border-left: 0;
#     border-right: 0;
#     border-top: transparent;
#     border-bottom: 1px solid #999;
#     outline: none;
#     background: transparent;
# }  
# .submit-btn{
#     /* font-size: 20px; */
#     width:85%;
#     padding: 10px 30px;
#     cursor: pointer;
#     display: block;
#     margin: auto;
#     background: linear-gradient(to right,#ff105f,#ffad06);
#     border: 0;
#     outline: none;
#     border-radius: 30px;
# }
# .check-box{
#     margin: 30px 10px 30px 0;
# }
# span{
#     color: #777;
#     font-size: 12px;
#     bottom: 68px;
#     position: absolute; 
# }
# #login{
#     left:  50px;

# }
# #signin{
#     left:  450px;

# }  
# .company-name{
#     text-align: center;
#     width:35%;
#     padding: 10px 30px;
#     cursor: pointer;
#     display: block;
#     margin: auto;
#     background: linear-gradient(to right,#ff105f,#ffad06);
#     border: 0;
#     outline: none;
#     border-radius: 30px;

# }
# </style>
# </head>
# <body>
#     <div class="hero"> 
#        <img src="banner.jpg"  >
#         <div class="form-box">
#             <div class="button-box"> 
#                 <div id="btn"></div>
#                 <button type="button" class="toggle-btn" onclick="login()">Log In</button>
#                 <button type="button" class="toggle-btn" onclick="signin()" >Sign In</button>
#             </div>
            

#              <div class="company-name">
#                 <h4>AI MATIC</h4>
#                 <!-- <img src="fb.png" alt="facebook logo">
#                 <img src="tw.png" alt="twitter logo">
#                 <img src="gp.png" alt="google logo"> -->
#             </div>
#             <form id="login" class="input-group">
#               <input type="text" class="input-field" placeholder="User Id" required >
#               <input type="text" class="input-field" placeholder="Enter Password" required >
#               <input type="checkbox" class="check-box"><span>Remember Password</span>
#               <button type="submit" class="submit-btn">Log in</button> 
#             </form>
#             <form id="signin" class="input-group">
#                 <input type="text" class="input-field" placeholder="User Id" required >
#                 <input type="email" class="input-field" placeholder="Email Id" required >
#                 <input type="text" class="input-field" placeholder="Enter password" required >
#                 <input type="checkbox" class="check-box"><span>I agree to the terms </span>
#                 <button type="submit" class="submit-btn">Sign In</button> 
#             </form>
#         </div> 
#     </div>
#     <!-- <script src="scripts.js"></script> -->
#     <script >
#       var x = document.getElementById("login");
#         var y = document.getElementById("signin");
#         var z = document.getElementById("btn");
#         function signin(){
#             x.style.left="-400px";
#             y.style.left="50px";
#             z.style.left="110px";
#         }
#         function login(){
#             x.style.left="50px";
#             y.style.left="450px";
#             z.style.left="0px";
#         } 
#     </script>
# </body>
# </html>
#     """
#     return HTMLResponse(content=html_content, status_code=200)