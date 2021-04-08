Imports System.IO
Imports ExcelDataReader

Public Class Form1
    Dim tables As DataTableCollection
    Private Sub BtBrowse_Click(sender As Object, e As EventArgs) Handles BtBrowse.Click
        Using ofd As OpenFileDialog = New OpenFileDialog()
            If ofd.ShowDialog() = DialogResult.OK Then
                TxtFileName.Text = ofd.FileName
                Using stream = File.Open(ofd.FileName, FileMode.Open, FileAccess.Read)
                    Using reader As IExcelDataReader = ExcelReaderFactory.CreateReader(stream)
                        Dim result As DataSet = reader.AsDataSet(New ExcelDataSetConfiguration() With {
                                                                 .ConfigureDataTable = Function(__) New ExcelDataTableConfiguration() With {
                                                                 .UseHeaderRow = True}})
                        tables = result.Tables
                        CBSheet.Items.Clear()
                        ComboBox1.Items.Clear()
                        For Each table As DataTable In tables
                            CBSheet.Items.Add(table.TableName)
                        Next

                        For Each table As DataTable In tables
                            ComboBox1.Items.Add(table.Columns)
                        Next


                    End Using
                End Using
            End If

        End Using
    End Sub

    Private Sub CBSheet_SelectedIndexChanged(sender As Object, e As EventArgs) Handles CBSheet.SelectedIndexChanged
        Dim dt As DataTable = tables(CBSheet.SelectedItem.ToString())
        DataGridView1.DataSource = dt
    End Sub

    Private Sub BtChart_Click(sender As Object, e As EventArgs) Handles BtForm2.Click

        Form2.Show()
    End Sub

    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged
        Dim dt As DataTable = tables(ComboBox1.SelectedItem.ToString())
    End Sub

    Private Sub BtOpenFile_Click(sender As Object, e As EventArgs) Handles BtOpenFile.Click
        Process.Start("Excel", TxtFileName.Text)
    End Sub
End Class
