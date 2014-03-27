#include <iostream>

#include <QWebView>
#include <QApplication>
#include <QString>
#include <QObject>


QString html = " \
<html> \
	<head> \
	</head> \
	<body> \
		Hello \
		<script> \
			alert(\"Good morning\") \
		</script> \
	</body> \
</html> \
";

class Bar : public QObject {
	Q_OBJECT

slots:
	void foo();
};

void Bar::foo() {
	std::cout
		<< "yup"
		<< std::endl
	;
}

int main(int argc, char** argv) {
	QApplication app(argc, argv);
	QWebView view;
	Bar b;

	QObject::connect(
		view.page()->mainFrame(), 
		SIGNAL(view.page()->mainFrame().javaScriptWindowObjectCleared()),
		b,
		SLOT(foo)
	);

	view.show();
	view.setHtml(html, QString(""));

	return app.exec();
}