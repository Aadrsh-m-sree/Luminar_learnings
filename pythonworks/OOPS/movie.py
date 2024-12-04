class Movie:
    title:str
    rating:float
    runtime:int
    director:str
    genre:str

    def __init__(self,title,rating,runtime,director,genre):
        self.title=title
        self.rating=rating
        self.runtime=runtime
        self.director=director
        self.genre=genre
    
    def display_movie(self):
        print(f"Title :{self.title}")
        print(f"Director :{self.director}")
        print(f"Genre :{self.genre}")
        print(f"Runtime :{self.runtime}")
        print(f"Rating :{self.rating}")
        print()

Movie1=Movie("KGF",8.2,156,"Prashanth Neel","Action,Thriller")
Movie2=Movie("ARM",7.6,150,"Jithin Laal","Action,Adventure")

Movie1.display_movie()
Movie2.display_movie()