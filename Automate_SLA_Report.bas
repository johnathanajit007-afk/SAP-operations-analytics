Sub FormatSLADashboard()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    
    ' Header Formatting (Hilti Executive Red Theme)
    With ws.Range("A1:G1")
        .Font.Bold = True
        .Font.Color = rgbWhite
        .Interior.Color = RGB(210, 16, 52)
        .HorizontalAlignment = xlCenter
    End With
    
    ' Highlight Low SLA Breaches (< 85% OTIF)
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    Dim cell As Range
    For Each cell In ws.Range("F2:F" & lastRow)
        If cell.Value < 85.0 Then
            cell.Interior.Color = RGB(255, 204, 204)
            cell.Font.Color = RGB(153, 0, 0)
            cell.Font.Bold = True
        Else
            cell.Interior.Color = RGB(204, 255, 204)
        End If
    Next cell
    
    ws.Columns("A:G").AutoFit
    MsgBox "SLA Audit Report Successfully Formatted!", vbInformation, "Hilti Ops Analytics"
End Sub