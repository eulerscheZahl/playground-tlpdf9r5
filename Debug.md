# Debugging

This part is very specific to your programming language.
We reproduce an entire game now. If the error only occurs after 50 turn, you don't want to step there line by line. Depending on the possibilities of your language you could set a conditional breakpoint.
In C# you can also set a breakpoint in code:
`if (x == 13 && y == 3) System.Diagnostics.Debugger.Break();`.
Without a debugger, this statement will just be ignored. So you can even submit that line without timing out.

I also recommend to draw some images. They don't have to be pretty as long as they contain helpful data that you don't see easily on the CodinGame website.

I used the following code to draw some images for Ocean of Code:
``` csharp
int turn = 0;
public void DrawBoard(string opponentOrders)
{
    List<Cell> oppCells = OpponentTracker.CurrentCells();
    turn++;
    int cellSize = 50;
    Bitmap bmp = new Bitmap(cellSize * Width, cellSize * (Height + 1));
    using (Graphics g = Graphics.FromImage(bmp))
    {
        g.Clear(Color.SkyBlue);
        foreach (Cell cell in Grid)
        {
            if (cell.Blocked) g.FillRectangle(Brushes.LawnGreen, cellSize * cell.X, cellSize * cell.Y, cellSize, cellSize);
            else if (cell.Visited) g.FillRectangle(Brushes.Orange, cellSize * cell.X, cellSize * cell.Y, cellSize, cellSize);
            if (MineLocations.Contains(cell)) g.FillRectangle(Brushes.RoyalBlue, cellSize * cell.X + 10, cellSize * cell.Y + 10, cellSize - 20, cellSize - 20);
        }
        foreach (Cell cell in oppCells)
        {
            g.FillEllipse(Brushes.LightGray, cellSize * cell.X + 10, cellSize * cell.Y + 10, cellSize - 20, cellSize - 20);
        }
        foreach (Cell cell in MeTracker.CurrentCells())
        {
            g.FillEllipse(Brushes.OrangeRed, cellSize * cell.X + 20, cellSize * cell.Y + 20, cellSize - 40, cellSize - 40);
        }
        if (MyPosition != null) g.FillEllipse(Brushes.Red, cellSize * MyPosition.X, cellSize * MyPosition.Y, cellSize, cellSize);
        g.FillRectangle(Brushes.White, 0, cellSize * Height, cellSize * Width, cellSize);
        g.DrawString(opponentOrders, new Font(new FontFamily("Arial"), 20), Brushes.Black, 2 * cellSize, Height * cellSize + 5);
        for (int x = 0; x <= Width; x++) g.DrawLine(Pens.Black, x * cellSize, 0, x * cellSize, Height * cellSize);
        for (int y = 0; y <= Width; y++) g.DrawLine(Pens.Black, 0, y * cellSize, Height * cellSize, y * cellSize);

        foreach (Cell cell in Grid)
        {
            if (cell.Blocked) continue;
            Font font = new Font(new FontFamily("Arial"), 10);
            if (OpponentTracker.GetCandidates().Any(c => c.MineDrops.Any(d => d == cell))) font = new Font(font, FontStyle.Underline | FontStyle.Italic);
            g.DrawString(OpponentTracker.DangerLevel(cell).ToString("0.00"), font, Brushes.Black, 10 + cell.X * cellSize, 6 + cell.Y * cellSize);
        }
    }
    bmp.Save("img/" + turn.ToString("000") + ".png");
    bmp.Dispose();
}
```

This can be part of your bot, just make sure not to run it on submit:
``` csharp
#if DEBUG
            board.DrawBoard(opponentOrders);
#endif
```
