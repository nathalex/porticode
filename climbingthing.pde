int q = 0;
int w = 0;
Table table;
Table coordTable;
void setup()
{
  table = loadTable("coordinatesList.csv");
  coordTable = loadTable("optimalSolution.csv");
  size(1500,1500);
  scale(1, -1);
  translate(0, -height);
  fill(0,255,0);  
  for (int i = 0; i < 19; i++)
  {
    ellipse(table.getInt(i,0), table.getInt(i,1), 50,50 ); 
  }     
}

void draw()
{
  fill(0,0,255);
  ellipse(coordTable.getInt(w,0),1500 -  coordTable.getInt(w,1),60,60);
  delay(500);
  w++;
  if (w > 18)
  {
     w = 0; 
  } 
}
