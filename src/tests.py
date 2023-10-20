import helpers
import pytest
import yfinance as yf
import smaStrategy
import aoStrategy


def test_commandHelp():
    print("Command Help Test")
    try:
        helpers.input = lambda _: 'q'
        helpers.commandHelp()
        completed = True
    except BaseException:
        pytest.fail("Error in commandHelp()")
    assert completed is True


def test_smaPeriod():
    print("SMA Period Test")
    try:
        stock = yf.Ticker("AAPL")
        startDate = "2020-01-01"
        endDate = "2020-01-02"
        helpers.smaPeriod(stock, startDate, endDate)
        completed = True
    except BaseException:
        pytest.fail("Error in smaPeriod()")
    assert completed is True


def test_smaPrinter():
    print("SMA Printer Test")
    try:
        helpers.input = lambda _: 'q'
        stock = yf.Ticker("AAPL")
        startDate = "2020-01-01"
        endDate = "2020-01-02"
        actions = helpers.smaPeriod(stock, startDate, endDate)
        helpers.smaPrinter(actions)
        completed = True
    except BaseException:
        pytest.fail("Error in smaPrinter()")
    assert completed is True


def test_aoPeriod():
    print("AO Period Test")
    try:

        stock = yf.Ticker("AAPL")
        startDate = "2020-01-01"
        endDate = "2020-01-02"
        helpers.aoPeriod(stock, startDate, endDate)
        completed = True
    except BaseException:
        pytest.fail("Error in aoPeriod()")
    assert completed is True


def test_aoPrinter():
    print("AO Printer Test")
    try:
        helpers.input = lambda _: 'q'
        helpers.input = lambda _: 'q'
        stock = yf.Ticker("AAPL")
        startDate = "2020-01-01"
        endDate = "2020-01-02"
        actions = helpers.aoPeriod(stock, startDate, endDate)
        helpers.aoPrinter(actions)
        completed = True
    except BaseException:
        pytest.fail("Error in aoPrinter()")
    assert completed is True
