function createSmartTravelSurvey() {
  var form = FormApp.create('Smart Travel Assistant for Cambodia - User Survey');
  form.setDescription(
    'CADT Innovation Challenge Research\n\n' +
    'This anonymous survey explores travel challenges and interest in an AI-powered travel assistant for Cambodia.\n\nTime: 3–5 minutes.'
  );
  form.setConfirmationMessage('🎉 Thank you for completing our survey! Your responses will help improve our project.');

  form.addSectionHeaderItem().setTitle('Section 1: Personal Information');
  form.addMultipleChoiceItem().setTitle('1. What is your age?').setRequired(true)
    .setChoiceValues(['Under 18','18–24','25–34','35–44','45 or above']);
  form.addMultipleChoiceItem().setTitle('2. What best describes you?').setRequired(true)
    .setChoiceValues(['Cambodian','International Tourist','International Student','Expat Living in Cambodia','Other']);
  form.addMultipleChoiceItem().setTitle('3. How often do you travel within Cambodia?').setRequired(true)
    .setChoiceValues(['Weekly','Monthly','A few times a year','Rarely','Never']);

  form.addPageBreakItem().setTitle('Section 2: Current Travel Experience');
  form.addCheckboxItem().setTitle('4. Which travel applications do you usually use?')
    .setChoiceValues(['Google Maps','Booking.com','Agoda','TripAdvisor','Grab','Facebook','TikTok','Other']);
  form.addMultipleChoiceItem().setTitle('5. Do you usually switch between multiple apps while traveling?')
    .setChoiceValues(['Yes','No']).setRequired(true);
  form.addCheckboxItem().setTitle('6. What are the biggest challenges you face while traveling? (Choose up to 3)')
    .setChoiceValues(['Finding restaurants','Finding affordable hotels','Planning my travel budget','Heavy traffic','Finding tourist attractions','Language barriers','Public transportation','Using too many different apps','Other']);

  form.addPageBreakItem().setTitle('Section 3: Feature Importance');
  var grid=form.addGridItem();
  grid.setTitle('7. Please rate how important each feature is to you.');
  grid.setRows(['Restaurant Finder','Hotel Finder','Budget Planner','Tourist Attractions','Live Traffic Updates','AI Travel Assistant','Offline Maps','Emergency Contacts','Public Transportation Information']);
  grid.setColumns(['Not Important','Slightly Important','Neutral','Important','Very Important']);

  form.addPageBreakItem().setTitle('Section 4: AI Features');
  form.addMultipleChoiceItem().setTitle('8. Would you use an AI assistant that creates a travel plan based on your budget and interests?')
    .setChoiceValues(['Definitely Yes','Probably Yes','Not Sure','Probably No','Definitely No']);
  form.addMultipleChoiceItem().setTitle('9. Which AI feature would you use the most?')
    .setChoiceValues(['Personalized itinerary','Budget planning','Restaurant recommendations','Hotel recommendations','Route optimization','AI chatbot']);

  form.addPageBreakItem().setTitle('Section 5: Preferences');
  form.addCheckboxItem().setTitle('10. What matters most when choosing a restaurant?')
    .setChoiceValues(['Price','Reviews','Distance','Cuisine','Halal Food','Vegetarian Options','Open Now']);
  form.addMultipleChoiceItem().setTitle('11. What matters most when choosing a hotel?')
    .setChoiceValues(['Price','Location','Reviews','Facilities','Safety']);

  form.addPageBreakItem().setTitle('Section 6: Interest');
  form.addMultipleChoiceItem().setTitle('12. If this application were available today, would you use it?')
    .setChoiceValues(['Definitely','Probably','Maybe','Probably Not','Definitely Not']);
  form.addCheckboxItem().setTitle('13. Which feature would encourage you to download this application?')
    .setChoiceValues(['Everything in one app','AI trip planning','Budget planner','Offline maps','Hidden local attractions','Multi-language support','Emergency assistance','Public transportation information']);
  form.addScaleItem().setTitle('14. How likely are you to recommend this app to your friends or family?')
    .setBounds(1,5).setLabels('Very Unlikely','Very Likely');

  form.addPageBreakItem().setTitle('Section 7: Open Feedback');
  form.addParagraphTextItem().setTitle('15. What is the biggest problem you experience while traveling?');
  form.addParagraphTextItem().setTitle('16. What additional features would you like this application to have?');

  var ss=SpreadsheetApp.create('Smart Travel Assistant Survey Responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Form URL: '+form.getEditUrl());
  Logger.log('Published URL: '+form.getPublishedUrl());
  Logger.log('Responses Sheet: '+ss.getUrl());
}
