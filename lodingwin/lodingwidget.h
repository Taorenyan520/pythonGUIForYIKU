#ifndef LODINGWIDGET_H
#define LODINGWIDGET_H

#include <QWidget>

namespace Ui {
class LodingWidget;
}

class LodingWidget : public QWidget
{
    Q_OBJECT

public:
    explicit LodingWidget(QWidget *parent = 0);
    ~LodingWidget();

private slots:
    void on_pushButtonLog_clicked();

private:
    Ui::LodingWidget *ui;
};

#endif // LODINGWIDGET_H
