var Constants = {
  HOST_ENDPOINT : "http://ec2-107-22-137-168.compute-1.amazonaws.com",
  Business : {
    Search : '/demo/search',
    BusinessInfo : '/demo/business/'
  }
};

var Helpers = {
  getQueryParams : function () {
    
  },

  renderTemplate : function renderTemplate(templateNode, targetNode, data)
  {
    var source = templateNode.html(),
        template = Handlebars.compile(source);

    targetNode.append(template(data));
  }
};
