class JuegoVida:
  def __int__(self,rows,cols, generaciones, poblacion_inicial):
    
    
#Pruebas
def main():
  inicial=[[1,2],[2,1],[2,2],[2,3]]
  juego=JuegoVida(5,5,4,inicial)
  juego.to_string()
  for r in range(5):
    for c in range(5):
      print(f"[{r}][{c}]={juego.get_num_live_neighbours(r,c)}")
     
main()  
