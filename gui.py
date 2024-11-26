import wx

def show_selection_dialog(options):
    dialog = wx.SingleChoiceDialog(None, "Choose one of the options:", "Select an Option", options)

    if dialog.ShowModal() == wx.ID_OK:
        selected_option = dialog.GetStringSelection()
    else:
        selected_option = None
    dialog.Destroy()
    return selected_option
