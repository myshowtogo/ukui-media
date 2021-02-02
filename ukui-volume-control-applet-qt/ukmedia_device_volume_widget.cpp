/*
 * Copyright (C) 2019 Tianjin KYLIN Information Technology Co., Ltd.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, see <http://www.gnu.org/licenses/&gt;.
 *
 */
#include "ukmedia_device_volume_widget.h"
#include <QWidget>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QSpacerItem>
#include <QDebug>
#include "customstyle.h"
UkmediaDeviceWidget::UkmediaDeviceWidget(QWidget *parent) : QWidget (parent)
{
    setAttribute(Qt::WA_TranslucentBackground);
    //初始化设备界面
    displayOutputLabel = new QLabel(this);
    deviceWidget = new QWidget(this);
    outputWidget = new QWidget(deviceWidget);
    outputSliderWidget = new QWidget(outputWidget);
    inputWidget = new QWidget(deviceWidget);
    inputSliderWidget = new QWidget(inputWidget);

    inputDeviceLabel = new QLabel(tr("Input Device"),this);
    inputDeviceDisplayLabel = new QLabel(inputWidget);
    inputDeviceBtn = new QPushButton(inputWidget);
    inputDeviceSlider = new UkmediaVolumeSlider(inputSliderWidget,true);
    inputMuteButton = new UkuiButtonDrawSvg(inputSliderWidget);

    outputWidget->setFixedSize(340,66);
    outputSliderWidget->setFixedSize(306,32);
    outputMuteBtn = new UkuiButtonDrawSvg(outputSliderWidget);
    outputDeviceLabel = new QLabel(tr("Output Device"),this);
    outputDeviceDisplayLabel = new QLabel(outputWidget);
    outputDeviceBtn = new QPushButton(outputWidget);
    outputDeviceSlider = new UkmediaVolumeSlider(outputSliderWidget,true);
    noInputDeviceLabel = new QLabel(tr("Input device can not be detected"),this);
    outputDisplayVolumeLabel = new QLabel(this);

    noInputDeviceLabel->setFixedSize(320,24);
    QPalette palete = outputDeviceBtn->palette();
    palete.setColor(QPalette::Highlight,Qt::transparent);
    palete.setBrush(QPalette::Button,QBrush(QColor(1,1,1,0)));
    outputDeviceBtn->setPalette(palete);
    outputMuteBtn->setFixedSize(24,24);
    inputMuteButton->setFixedSize(24,24);
    QSize iconSize(24,24);
    outputMuteBtn->setIconSize(iconSize);
    inputMuteButton->setIconSize(iconSize);
    inputDeviceBtn->setFocusPolicy(Qt::NoFocus);
    outputDeviceBtn->setFocusPolicy(Qt::NoFocus);
    noInputWidgetInit();

    inputDeviceBtn->setStyleSheet("QPushButton{background:transparent;border:0px;"
                                "padding-left:0px;}");
    outputDeviceBtn->setStyleSheet("QPushButton{background:transparent;border:0px;"
                                 "padding-left:0px;}");
}



void UkmediaDeviceWidget::noInputWidgetInit()
{
    //隐藏inputDeviceWidget
    inputDeviceLabel->hide();
    inputWidget->hide();
    inputSliderWidget->hide();
    noInputDeviceLabel->show();
    QSize iconSize(32,32);
    //设置输入输出音量图标
    outputDeviceBtn->setFixedSize(iconSize);
    outputDeviceBtn->setIconSize(iconSize);
#if (QT_VERSION <= QT_VERSION_CHECK(5,12,1))
    outputDeviceBtn->setIcon(QIcon("/usr/share/icons/ukui-icon-theme-classical/scalable/devices/audio-card.svg"));
#elif (QT_VERSION > QT_VERSION_CHECK(5,6,1))
    outputDeviceBtn->setIcon(QIcon("/usr/share/ukui-media/img/audiocard.svg"));
#endif
  //设置滑动条的范围和取向
    outputDeviceLabel->setFixedSize(140,24);
    outputDeviceDisplayLabel->setFixedSize(300,24);

    outputDeviceSlider->setRange(0,100);
    outputDeviceSlider->setOrientation(Qt::Horizontal);
    outputDeviceSlider->setFixedSize(220,22);
    deviceWidget->setFixedSize(358,320);

    QHBoxLayout *hlayout = new QHBoxLayout;
    QVBoxLayout *vlayout = new QVBoxLayout;
    QSpacerItem *item1 = new QSpacerItem(18,20);
    QSpacerItem *item2 = new QSpacerItem(12,20);

    //输出设备布局outputWidget
    hlayout->addWidget(outputDeviceBtn);
    hlayout->addItem(item1);
    hlayout->addWidget(outputDeviceSlider);
    hlayout->addItem(item2);
    hlayout->addWidget(outputMuteBtn);
    hlayout->setSpacing(0);
    outputSliderWidget->setLayout(hlayout);
    outputSliderWidget->layout()->setContentsMargins(0,0,0,0);

    vlayout->addWidget(outputDeviceDisplayLabel);
    vlayout->addWidget(outputSliderWidget);
    vlayout->setSpacing(12);
    outputWidget->setLayout(vlayout);
    outputWidget->layout()->setContentsMargins(0,0,0,0);
    outputDeviceLabel->move(18,22);
    outputWidget->move(18,62);
    noInputDeviceLabel->move(18,154);
}

void UkmediaDeviceWidget::inputWidgetShow()
{
    //设置noinputlabel隐藏
    noInputDeviceLabel->hide();
    const QSize iconSize(32,32);
    inputWidget->setFixedSize(340,74);
    inputSliderWidget->setFixedSize(306,32);

    //设置输入输出音量图标
    inputDeviceBtn->setFixedSize(iconSize);
    inputDeviceBtn->setIconSize(iconSize);
#if (QT_VERSION <= QT_VERSION_CHECK(5,12,1))
    inputDeviceBtn->setIcon(QIcon("/usr/share/icons/ukui-icon-theme-classical/scalable/devices/audio-input-microphone.svg"));
#elif (QT_VERSION > QT_VERSION_CHECK(5,6,1))
    inputDeviceBtn->setIcon(QIcon("/usr/share/ukui-media/img/audio-input-microphone.svg"));
#endif
    //设置滑动条的范围和取向
    inputDeviceLabel->setFixedSize(140,24);
    inputDeviceDisplayLabel->setFixedSize(220,24);

    inputDeviceSlider->setRange(0,100);
    inputDeviceSlider->setOrientation(Qt::Horizontal);
    inputDeviceSlider->setFixedSize(220,22);
    //布局
    QHBoxLayout *hlayout = new QHBoxLayout;
    QVBoxLayout *vlayout = new QVBoxLayout;

    //输入设备布局 inputWidget
    hlayout->addWidget(inputDeviceBtn);
    hlayout->addItem(new QSpacerItem(18,20));
    hlayout->addWidget(inputDeviceSlider);
    hlayout->addItem(new QSpacerItem(12,20));
    hlayout->addWidget(inputMuteButton);
    hlayout->setSpacing(0);
    inputSliderWidget->setLayout(hlayout);
    inputSliderWidget->layout()->setContentsMargins(0,0,0,0);

    vlayout->addWidget(inputDeviceDisplayLabel);
    vlayout->addWidget(inputSliderWidget);
    vlayout->setSpacing(14);
    vlayout->setContentsMargins(0,0,0,6);
    inputWidget->setLayout(vlayout);

    inputDeviceLabel->move(18,154);
    inputWidget->move(18,194);

    inputDeviceLabel->show();
    inputSliderWidget->show();
    inputWidget->show();
}

void UkmediaDeviceWidget::inputWidgetHide()
{
    //隐藏inputDeviceWidget
    inputDeviceLabel->hide();
    inputWidget->hide();
    inputSliderWidget->hide();
    noInputDeviceLabel->show();
}


UkmediaDeviceWidget::~UkmediaDeviceWidget()
{

}
