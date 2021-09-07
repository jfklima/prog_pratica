(defun executa-python-and-open-relatorio-python ()
  (interactive)
  (python-shell-send-buffer)
  (find-file "relatorio.txt"))
