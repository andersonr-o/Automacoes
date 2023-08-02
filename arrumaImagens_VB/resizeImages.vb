Sub PosicionarImagens()
    Dim doc As Document
    Dim imagens As InlineShapes
    Dim imagem As InlineShape
    
    ' Define o documento ativo
    Set doc = ActiveDocument
    
    ' Verifica se há pelo menos 30 imagens no documento
    If doc.InlineShapes.Count < 3 Then
        MsgBox "O documento não contém pelo menos 30 imagens.", vbExclamation
        Exit Sub
    End If
    
    ' Define as imagens
    Set imagens = doc.InlineShapes
    
    ' Define a largura da página
    Dim larguraPagina As Single
    larguraPagina = doc.PageSetup.PageWidth - doc.PageSetup.LeftMargin - doc.PageSetup.RightMargin
    
    ' Define a altura da página
    Dim alturaPagina As Single
    alturaPagina = doc.PageSetup.PageHeight - doc.PageSetup.TopMargin - doc.PageSetup.BottomMargin
    
    ' Define a altura e a posição das imagens
    For Each imagem In imagens
        imagem.LockAspectRatio = msoFalse
        imagem.Width = larguraPagina
        imagem.Height = alturaPagina * 0.48
        imagem.Range.ParagraphFormat.Alignment = wdAlignParagraphLeft
        imagem.Range.ParagraphFormat.SpaceBefore = 0
        imagem.Range.ParagraphFormat.SpaceAfter = alturaPagina * 0.5
    Next imagem
    
    ' Move o cursor para a posição após a última imagem
    Selection.EndKey Unit:=wdStory
End Sub