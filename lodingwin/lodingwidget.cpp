#include "lodingwidget.h"
#include "ui_lodingwidget.h"

LodingWidget::LodingWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::LodingWidget)
{
    ui->setupUi(this);
}

LodingWidget::~LodingWidget()
{
    delete ui;
}

void LodingWidget::on_pushButtonLog_clicked()
{

}
