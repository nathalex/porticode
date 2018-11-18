int q = 0;
int w = 1;
Table table;
Table coordTable;
int limit;
int numHolds;
int holdLimb = 0;
int scaleBackground;
//PImage = rock;

void setup()
{
  table = loadTable("coordinatesList.csv");
  coordTable = loadTable("optimalSolution.csv");
  limit = coordTable.getInt(0,0);
  numHolds = table.getInt(0,0);
  scaleBackground = table.getInt(0,1);
  size(500,500);
  scale(1, -1);
  translate(0, -height);
  fill(0,255,0);  
  //rock = loadImage("rockWallExample.jpg");
  //rock.resize(
  for (int i = 0; i < numHolds; i++)
  {
    ellipse(table.getInt(i,0), table.getInt(i,1), 25,25 ); 
  }     
}
void draw()
{
  fill(0,0,255);
  ellipse(coordTable.getInt(w,0),500 -  coordTable.getInt(w,1),20,20);
  if (holdLimb < limit)
  {
    fill(0,0,0);
    if (holdLimb%4 == 0)
    
    {
      text("LF", 20+coordTable.getInt(w,0),500 -  coordTable.getInt(w,1));
    }
    else if(holdLimb%4 == 1)
    {
      text("RF", 20+coordTable.getInt(w,0),500 -  coordTable.getInt(w,1));
    }
    else if(holdLimb%4 == 2)
    {
      text("LH",20+ coordTable.getInt(w,0),500 -  coordTable.getInt(w,1));
    }
    else if(holdLimb%4 == 3)
    {
      text("RH",20 + coordTable.getInt(w,0),500 -  coordTable.getInt(w,1));
    }
    holdLimb++;
  }
  delay(500);
  w++;
  if (w > limit)
  {
     w = 0; 
  } 
}
