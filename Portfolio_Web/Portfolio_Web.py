import reflex as rx 

twitter_image="gorjeo.png"
"IMAGEN EN :" "https://www.flaticon.es/iconos-gratis/pio"
linkedin_image="linkedin.png"
"IMAGEN EN :" "https://www.flaticon.es/iconos-gratis/linkedin"
github_image="github_logo.png"
"IMAGEN EN :" "https://www.flaticon.es/iconos-gratis/gato"
house_price="house_predictor.jpg"
data_base="databasequery.png"
url1="https://houseprice-predictor.streamlit.app/"
url2="https://databasequery.streamlit.app/"

class State (rx.State):

    pass

text:dict={
    "texto":{
                "_light":{
                    "font_style":"oblique",
                    "font_weight":"normal",
                    "font_family":"fantasy",
                    "font_size":"1.5em",
                    "color":"#4e4646",

                    },
                "_dark":{                    
                    "font_style":"oblique",
                    "font_weight":"normal",
                    "font_family":"fantasy",
                    "font_size":"1.5em",
                    "color":"#9e9e9e",
                    },
    },
    "heading":{
                "font_size":["2rem","2.85rem", "4rem","5rem","5rem"],
                "font_weight":"500",
                "_dark":{
                    "background":"linear-gradient(to right, #e1e1e1,#757575)",
                    "background_clip":"text",
                },
                "_light":{
                    "background": "#6AA3CF",
                    "background": "repeating-linear-gradient(to right, #6AA3CF 0%, #231421 100%)",
                    "-webkit-background-clip": "text",
                    "-webkit-text-fill-color": "transparent", 
                },

    },
    
    "markdown":{
            "_light":{
                "background": "#62B4FC",
                "background": "linear-gradient(to top left, #62B4FC 0%, #231421 66%)",
                "-webkit-background-clip": "text",
                "-webkit-text-fill-color": "transparent",
        },
            "_dark":{
                "background": "#CFCFCF",
                "background": "linear-gradient(to top, #CFCFCF 0%, #698DA6 100%)",
                "-webkit-background-clip": "text",
                "-webkit-text-fill-color": "transparent",
            }
    }
}

dots:dict={
    "@keyframes dots":{
        "0%":{"background_position":"0 0"},
        "100%":{"background_position":"40px 40px"},
    },
    "animation":"dots 4s linear infinite alternate-reverse both",
}

wave:dict={
    "@keyframes wave":{
        "0%":{"transform":"rotate(45deg)"},
        "100%":{"transform":"rotate(-15deg)"},
    },
    "animation":"wave 0.8s cubic-bezier(0.25,0.46,0.45,0.94) infinite alternate-reverse both",

}
css:dict={
    "app":{
        "_dark":{
            "bg":"#0e0e13"
        }
    },
    "header": {
        "widht":"100%",
        "height":"50px",
        "padding":[
            "0rem 1rem",
            "0rem 1rem",
            "0rem 1rem",                
            "0rem 1rem",
            "0rem 1rem",
        ],
        "transition":"all 550ms ease"
    },
    "main":{
        "property":{
            "widht":"100%",
            "height":"84vh",
            "padding":"15rem 0rem",
            "align_items":"center",
            "justify_content":"start",

        }
    },
    "footer":{
        "widht":["100%","90%","60%","45%","45%"],
        "height":"50px",
        "alignt_items":"center",
        "justify_content":"center",
    }

}

class Header:
    def __init__(self):
        self.Header: rx.Hstack=rx.hstack(style=css.get("header"))
        self.email: rx.Hstack=rx.hstack(
            rx.box(
                rx.icon(
                    tag="email",_dark={"color": "rgba(255,255,255,0.5)"},)),
                    rx.box(
                        rx.text(
                            "juanglezm3@gmail.com",_dark={"color":"rgba(255,255,255,0.5)"}
                            )
                            ),
                            align_items="center",
                            justify_content="center",
                            
        )
        self.theme: rx.Component=rx.color_mode_button(
            rx.color_mode_icon(),
            color_scheme="gray",
            _light={"color":"black"},
            _dark={"color":"white"},
            
        )

    def compile_component(self) ->list[rx.Hstack]:
        return [self.email,rx.spacer(),self.theme]

    def build(self) ->rx.Hstack:
        self.Header.children=self.compile_component()
        return self.Header

class Main:
    def __init__ (self):
        self.box: rx.Box=rx.box(widht="100%")
        self.name:rx.Hstack=rx.hstack(
            rx.heading(
                "Hi - I'm Juan Gonzalez",
                font_size=["1.25em","1.5em","2em","2.5em", "3em","3.5em","4em","4.5em","5em"],
                font_weight="900",
                _dark={
                    "background":"linear-gradient(to right, #e1e1e1,#757575)",
                    "background_clip":"text",
                },
            ),
            rx.heading(
                "👋",
                size="2xl",
                style=wave,
                font_size=["1.25em","1.5em","2em","2.5em", "3em","3.5em","4em","4.5em","5em"],
                ),
            spacing="1.75rem",
            
        )
        self.badge_stack_max: rx.Hstack=rx.hstack(spacing="1rem")
        self.badge_stack_min: rx.Vstack=rx.vstack(spacing="1.25rem")
        titles: list=["ML Engineer","Python Developer","Business Intelligence Analyst"]
        self.badge_stack_max.children=[self.create_badges(title) for title in titles]
        self.badge_stack_min.children=[self.create_badges(title) for title in titles]

        self.crumbs: rx.Breadcrumb=rx.breadcrumb()
        data:list=[
            [github_image,"GitHub","https://github.com/JuanGM07"],
            [twitter_image,"Twitter","https://twitter.com/TranslatorData"],
            [linkedin_image,"LinkedIn","https://www.linkedin.com/in/juan-gonz%C3%A1lez-moreno-207127283/"],
        ]
        self.crumbs.children=[
            self.create_breadcrumb_item(path,title,url)for path,title,url in data
                              ]
    def create_breadcrumb_item(self,path:str,title:str,url:str | None)->rx.Component:
        return rx.breadcrumb_item(
            rx.hstack(
                rx.image(src=path,
                        html_width="24px",
                        html_height="24px",
                        _dark={"filter":"brightness(0) invert(1)"},
                        ),
                        rx.breadcrumb_link(
                            title,
                            href=url,
                            _dark={"color":"rgba(255,255,255,0.7)"}
                        ),
            )
        )

    def create_badges(self, title:str) ->rx.Component:
        return rx.badge(
            title,
            variant="solid",
            padding=[
                "0.15rem 0.35rem",
                "0.15rem 0.35rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
            ],

        )

    def compile_desktop_component(self) ->rx.Component:
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                self.badge_stack_max,
                self.crumbs,
              
                style=css.get("main").get("property"),
                )
            )
        
    def compile_mobile_component(self) ->callable(rx.Component):
        return rx.mobile_only(
            rx.vstack(
                self.name,
                self.badge_stack_min,
                self.crumbs,
                
                style=css.get("main").get("property"),
            )
        )   

    def build (self) ->rx.Box:
        self.box.children=[self.compile_desktop_component(),
                           self.compile_mobile_component(),
                           ]
        return self.box

class Me_section:
    def __init__(self)->rx.Component:
        self.box: rx.Box=rx.box(widht="100%")
        self.me_section:rx.Vstack=rx.vstack(
            rx.heading(
                "Who am I?",
                style=text.get("heading"),
                
            ),
            rx.box(
                rx.text(
                    """
                    Hi I am Juan Gonzalez and I am 20 years old. I am currently studying mechanical engineering, 
                    but my passion is programming and computer science. Right now my focus is on creating ML models trough 
                    free APIS or free DB, trying to solve a problem that could happen in real life. Then I deploy it, on some 
                    cloud platform, or maybe only as an insight in some BI platform like tableau.
                    """,
                    style=text.get("texto"),
                    
                ),
                widht="100%",
                padding="20",
                font_size=["0.5em","0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],

            ),
            rx.flex(
                rx.vstack(
                    rx.box(rx.markdown("## My Skills"),
                           style=text.get("markdown"),
                            font_size=["0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],

                           ),
                    rx.box(
                        rx.text("➱Python",style=text.get("texto"),),
                        rx.text("➱SQL",style=text.get("texto"),),
                        rx.text("➱Scikit-Learn",style=text.get("texto"),),
                        rx.text("➱Tableau",style=text.get("texto"),),
                        width="130px",
                        align_items="right",
                    ),
                    font_size=["0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],
                    align_items="center",
                    
                ),
                rx.vstack(
                    rx.box(rx.markdown("## Learning..."),
                        style=text.get("markdown"),
                        ),
                    rx.box(
                        rx.text("➱Tensor Flow",style=text.get("texto"),),
                        rx.text("➱AWS",style=text.get("texto"),),
                        rx.text("➱Airflow",style=text.get("texto"),),
                        width="200px",
                    ),
                    font_size=["0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],
                    align_items="center",
                ),
            
            ),
            rx.heading(
                "What I do?",
                style=text.get("heading"),
                padding="2rem",
            ),
            rx.box(
                rx.text("""
                        1. First of all, I put me in the situation that I have to solve a problem. The company where I am working 
                        needs to sell more, spend less, or any problem that I could imagine 
                        (obviously this process in real life has to be solved with information that I would have if I would work in that company).

                        """,
                        style=text.get("texto"),
                        margin_bottom="20px"),
                rx.text("""
                        2. Then I get the data connecting to a free API, a database, csv, xslx, or any other file with others formats.

                        """,
                        style=text.get("texto"),
                        margin_bottom="20px"),

                rx.text("""
                        3. Later, I transform this unstructured data with a pipeline formed with a lot of processes and fuctions, like convert it with
                        pandas in a dataframe, impute nulls with the mean or median, perhaps separate the categorical data from the numeric one, or map the categorical data and transform it into numerical data.

                        """,
                        style=text.get("texto"),
                        margin_bottom="20px"),
                rx.text("""
                        4. When all my data is structured and clean. I divide it in training data and test data. Then I select a couple of algorithms that I think
                        that would bring me an accurated solution and I ajust the hyperparameters to find the best solution. This step provides me with a trained algorithm that solves my problem
                        (with a small error obviously).

                        """,
                        style=text.get("texto"),
                        margin_bottom="20px"),
                rx.text("""
                        5. Having a trained algorithm that solves my problem, allows me to put it in production, integrated with a simple UI, making predictions of new data.
                        Or maybe the aim wasn't to make this, we only needed a dashboard with insights that will allow the executives to make better decisions.
                        In that case I would do it with tableau.

                        """,
                        style=text.get("texto"),
                        margin_bottom="20px"),
                        padding="20", 
                        font_size=["0.5em","0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],
                        widht="100%",


            ),
            rx.heading(
                "Projects",
                style=text.get("heading"),
                padding="2rem",
            ),
            rx.box(
                rx.text(
                    """
                    I dont have experience in any company, but I worked in open source projects, and I had also make some projects to prove
                    my knolewdge on all that I said in the last section.
                    """,
                    style=text.get("texto"),
                    

                ),
                widht="100%",
                padding="20",
                align_items="center",
                justify_content="center",
                font_size=["0.5em","0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],
            ),
            rx.hstack(
                rx.link("House Price Predictor",href=url1,margin_bottom="50px",style=text.get("markdown"),font_size=["2em","2.5em", "3em","3.5em"],),
                
            ),
            rx.vstack(
                rx.image(
                    src=house_price,
                    html_width="500px",
                    html_height="500px",
                    border_radius="20px",
                    border= "5px solid #4D7387",
                    margin_bottom="30px",
                    align_items="center",
                    justify_content="center",
            ),
                margin_right= "800px",
                                     ),
            rx.vstack(
                rx.text("A house price predictor model based on the prices of the real state market of California.",
                style=text.get("texto"),
                align_items="center",
                justify_content="center",
                margin_bottom="40px",
                

                ),  
                font_size=["0.5em","0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],
                padding="10",
             
),
            rx.hstack(
                rx.link("Data Base Query",href=url2,margin_bottom="50px",style=text.get("markdown"),font_size=["2em","2.5em", "3em","3.5em"],),
                 ),
            rx.vstack(
                rx.image(
                    src=data_base,
                    html_width="500px",
                    html_height="500px",
                    border_radius="20px",
                    border= "5px solid #4D7387",
                    margin_bottom="30px",
                    align_items="center",
                    justify_content="center",
            ),
                margin_right= "800px",
                                     ),
            rx.vstack(
                rx.text("A NL2SQL model to query a data base through the OpenAI API.",
                style=text.get("texto"),
                align_items="center",
                justify_content="center",
                padding="10",

                ), 
                font_size=["0.5em","0.6em","0.7em","0.8em","0.9em","1em","1.1em","1.2em"],
              
),
               
            )
    def compile_desktop_component(self) ->rx.Component:
        return rx.tablet_and_desktop(
            rx.vstack(
                self.me_section
                )
            )
        
    def compile_mobile_component(self) ->callable(rx.Component):
        return rx.mobile_only(
            rx.vstack(
                self.me_section
            )
        )   

    def build (self) ->rx.Box:
        self.box.children=[self.compile_desktop_component(),
                           self.compile_mobile_component(),
                           ]
        return self.box
                
        
        

class Footer:
    def __init__(self)->None:
        self.footer:rx.Hstack=rx.hstack(style=css.get("footer"))
        self.footer.children.append(
            rx.text(
                "Copyright 2024 Juan Gonzalez",
                font_size="10px",
                font_weight="semibold",
            )

        )
  
    def build(self):
        return self.footer

@rx.page(route="/")
def landing() ->rx.Component:
    rx.script("document.documentElement.lang='es'"),
    header: object=Header().build()
    main: object=Main().build()
    footer: object=Footer().build()
    me_section: object=Me_section().build()
    return rx.vstack(
        header,
        main,
        me_section,
        footer,
        
        _light={
            "background":"radial-gradient(circle,rgba(0,0,0,0.35) 1px, transparent 1px)",
            "background_size":"25px 25px",
        },
        background="radial-gradient(circle,rgba(255,255,255,0.09) 1px, transparent 1px)",
        background_size="25px 25px",
        style=dots,
    )

app=rx.App(style=css.get("app"))
