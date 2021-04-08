<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim ChartArea1 As System.Windows.Forms.DataVisualization.Charting.ChartArea = New System.Windows.Forms.DataVisualization.Charting.ChartArea()
        Dim Legend1 As System.Windows.Forms.DataVisualization.Charting.Legend = New System.Windows.Forms.DataVisualization.Charting.Legend()
        Dim Series1 As System.Windows.Forms.DataVisualization.Charting.Series = New System.Windows.Forms.DataVisualization.Charting.Series()
        Me.DataGridView1 = New System.Windows.Forms.DataGridView()
        Me.label1 = New System.Windows.Forms.Label()
        Me.BtBrowse = New System.Windows.Forms.Button()
        Me.TxtFileName = New System.Windows.Forms.TextBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.CBSheet = New System.Windows.Forms.ComboBox()
        Me.BtForm2 = New System.Windows.Forms.Button()
        Me.Chart1 = New System.Windows.Forms.DataVisualization.Charting.Chart()
        Me.ComboBox1 = New System.Windows.Forms.ComboBox()
        Me.BtOpenFile = New System.Windows.Forms.Button()
        CType(Me.DataGridView1, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.Chart1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridView1
        '
        Me.DataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridView1.Location = New System.Drawing.Point(12, 12)
        Me.DataGridView1.Name = "DataGridView1"
        Me.DataGridView1.RowHeadersWidth = 51
        Me.DataGridView1.RowTemplate.Height = 24
        Me.DataGridView1.Size = New System.Drawing.Size(776, 325)
        Me.DataGridView1.TabIndex = 0
        '
        'label1
        '
        Me.label1.AutoSize = True
        Me.label1.Location = New System.Drawing.Point(32, 353)
        Me.label1.Name = "label1"
        Me.label1.Size = New System.Drawing.Size(71, 17)
        Me.label1.TabIndex = 1
        Me.label1.Text = "File Name"
        '
        'BtBrowse
        '
        Me.BtBrowse.Location = New System.Drawing.Point(713, 353)
        Me.BtBrowse.Name = "BtBrowse"
        Me.BtBrowse.Size = New System.Drawing.Size(75, 23)
        Me.BtBrowse.TabIndex = 2
        Me.BtBrowse.Text = "Browse"
        Me.BtBrowse.UseVisualStyleBackColor = True
        '
        'TxtFileName
        '
        Me.TxtFileName.Location = New System.Drawing.Point(108, 353)
        Me.TxtFileName.Name = "TxtFileName"
        Me.TxtFileName.ReadOnly = True
        Me.TxtFileName.Size = New System.Drawing.Size(599, 22)
        Me.TxtFileName.TabIndex = 3
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(32, 391)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(57, 17)
        Me.Label2.TabIndex = 4
        Me.Label2.Text = "Sheet : "
        '
        'CBSheet
        '
        Me.CBSheet.FormattingEnabled = True
        Me.CBSheet.Location = New System.Drawing.Point(108, 391)
        Me.CBSheet.Name = "CBSheet"
        Me.CBSheet.Size = New System.Drawing.Size(121, 24)
        Me.CBSheet.TabIndex = 5
        '
        'BtForm2
        '
        Me.BtForm2.Location = New System.Drawing.Point(713, 392)
        Me.BtForm2.Name = "BtForm2"
        Me.BtForm2.Size = New System.Drawing.Size(75, 23)
        Me.BtForm2.TabIndex = 6
        Me.BtForm2.Text = "Form2"
        Me.BtForm2.UseVisualStyleBackColor = True
        '
        'Chart1
        '
        ChartArea1.Name = "ChartArea1"
        Me.Chart1.ChartAreas.Add(ChartArea1)
        Legend1.Name = "Legend1"
        Me.Chart1.Legends.Add(Legend1)
        Me.Chart1.Location = New System.Drawing.Point(845, 12)
        Me.Chart1.Name = "Chart1"
        Series1.ChartArea = "ChartArea1"
        Series1.Legend = "Legend1"
        Series1.Name = "Quantity"
        Me.Chart1.Series.Add(Series1)
        Me.Chart1.Size = New System.Drawing.Size(558, 313)
        Me.Chart1.TabIndex = 7
        Me.Chart1.Text = "Chart1"
        '
        'ComboBox1
        '
        Me.ComboBox1.FormattingEnabled = True
        Me.ComboBox1.Location = New System.Drawing.Point(845, 353)
        Me.ComboBox1.Name = "ComboBox1"
        Me.ComboBox1.Size = New System.Drawing.Size(121, 24)
        Me.ComboBox1.TabIndex = 8
        '
        'BtOpenFile
        '
        Me.BtOpenFile.Location = New System.Drawing.Point(12, 455)
        Me.BtOpenFile.Name = "BtOpenFile"
        Me.BtOpenFile.Size = New System.Drawing.Size(125, 43)
        Me.BtOpenFile.TabIndex = 9
        Me.BtOpenFile.Text = "Open File"
        Me.BtOpenFile.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1443, 524)
        Me.Controls.Add(Me.BtOpenFile)
        Me.Controls.Add(Me.ComboBox1)
        Me.Controls.Add(Me.Chart1)
        Me.Controls.Add(Me.BtForm2)
        Me.Controls.Add(Me.CBSheet)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.TxtFileName)
        Me.Controls.Add(Me.BtBrowse)
        Me.Controls.Add(Me.label1)
        Me.Controls.Add(Me.DataGridView1)
        Me.MaximizeBox = False
        Me.Name = "Form1"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Read Excel .xls .xlsx file"
        CType(Me.DataGridView1, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.Chart1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents DataGridView1 As DataGridView
    Friend WithEvents label1 As Label
    Friend WithEvents BtBrowse As Button
    Friend WithEvents TxtFileName As TextBox
    Friend WithEvents Label2 As Label
    Friend WithEvents CBSheet As ComboBox
    Friend WithEvents BtForm2 As Button
    Friend WithEvents Chart1 As DataVisualization.Charting.Chart
    Friend WithEvents ComboBox1 As ComboBox
    Friend WithEvents BtOpenFile As Button
End Class
