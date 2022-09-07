from core.router import Router, Route, CallBack , public , private

router = Router("File Store Router",
                Route("Main Menu", "Main menu description ...",children=(
                        public("About me", callback=CallBack("public.utils", "about_us")),
                        public("Amir store", children=(
                                public("Sign in",callback=CallBack("public.utils" , "sign_in")),
                                public("Create User" ,  callback=CallBack("public.utils" , "Login")),
                                private("Manager" ,  children=(
                                    private("Add file",callback=CallBack("public.utils" , "add_file")),
                                    private("Back",callback=CallBack("core.router" , "back" , level = 2 )),
                                )),
                                public("Show the Files" , callback=CallBack("public.utils" ,"show_file")),
                                public("Show the comment" , callback=CallBack("public.utils" , "show_comment")),
                                private("Files" ,children=(
                                    private("Show the file" , callback=CallBack("public.utils" , "show_file")),
                                    private("order" , callback=CallBack("public.utils" , "order")),
                                    private("comment" , callback=CallBack("public.utils" , "comment")),
                                    private("Show the comment" , callback=CallBack("public.utils" , "show_comment")),
                                    private("Show order", callback=CallBack("public.utils", "show_order")),
                                    private("Back",callback=CallBack("core.router" , "back" , level = 2 )),
                                )),
                                private("Show order", callback=CallBack("public.utils", "show_order")),
                                private("sign_out", callback=CallBack("public.utils", "sign_out")),
    
                          )),
                      )
                      ))

