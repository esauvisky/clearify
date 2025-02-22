import wx
class SelectionDialog(wx.Dialog):
    def __init__(self, options, size=(400, 300)):
        super().__init__(None, title="Select an Option", size=size)

        self.selected_option = None
        self.refine_clicked = False
        self.refinement_prompt = None
        self.options = options

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a ListBox to display options
        self.list_box = wx.ListBox(self, choices=self.options, style=wx.LB_SINGLE)
        main_sizer.Add(self.list_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Create a TextCtrl for input
        self.input_field = wx.TextCtrl(self)
        main_sizer.Add(self.input_field, flag=wx.EXPAND | wx.ALL, border=10)

        self.SetSizerAndFit(main_sizer)

        # Bind events for key presses and close actions
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_press)
        self.Bind(wx.EVT_CLOSE, self.on_cancel)

    def on_key_press(self, event):
        keycode = event.GetKeyCode()

        if keycode == wx.WXK_ESCAPE:
            self.on_cancel(event)
        elif keycode == wx.WXK_RETURN:
            user_input = self.input_field.GetValue().strip()
            if user_input:
                # Use the input as a refinement prompt and clear existing options
                self.refinement_prompt = user_input
                self.EndModal(wx.ID_OK)
            else:
                # Accept the selected option if there is no input
                selection = self.list_box.GetSelection()
                if selection != wx.NOT_FOUND:
                    self.selected_option = self.list_box.GetString(selection)
                    self.EndModal(wx.ID_OK)
                else:
                    wx.MessageBox("Please select an option or provide input.", "No Selection", wx.OK | wx.ICON_INFORMATION)
        else:
            event.Skip()

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)
        self.Destroy()  # Close the dialog window


def show_selection_dialog(options):
    dialog = SelectionDialog(options, size=(10 * len(options[0]), 100 + len(options) * 30))
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        if dialog.refinement_prompt:
            return dialog.refinement_prompt, 'refine'
        else:
            return dialog.selected_option, 'ok'
    else:
        return None, 'cancel'


def show_refine_dialog():
    dialog = wx.TextEntryDialog(None, "Enter refinement instructions:", "Refine Options")
    if dialog.ShowModal() == wx.ID_OK:
        instructions = dialog.GetValue()
        dialog.Destroy()
        return instructions
    else:
        dialog.Destroy()
        return None
